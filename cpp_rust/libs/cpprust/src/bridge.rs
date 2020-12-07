#[cxx::bridge(namespace = "cpprust")]
mod ffi {
    struct BlobMetadata {
        size: usize,
        tags: Vec<String>,
    }

    struct Chunk {
        bytes: Vec<u8>,
    }

    // An iterator over contiguous chunks of a discontiguous file object. Toy
    // implementation uses a Vec<Vec<u8>> but in reality this might be iterating
    // over some more complex Rust data structure like a rope, or maybe loading
    // chunks lazily from somewhere.
    pub struct MultiBuf {
        chunks: Vec<Chunk>,
        pos: usize,
    }

    extern "Rust" {
        fn new_multi_buf(chunks: Vec<Chunk>) -> MultiBuf;
        fn next_chunk(buf: &mut MultiBuf) -> &[u8];
    }

    unsafe extern "C++" {
        include!("cpprust/include/cpprust/blobstore.hpp");

        type BlobstoreClient;

        fn new_blobstore_client() -> UniquePtr<BlobstoreClient>;

        fn put(&self, parts: &mut MultiBuf) -> u64;
        fn tag(&self, blobid: u64, tag: &str);
        fn metadata(&self, blobid: u64) -> BlobMetadata;
    }
}

impl ffi::Chunk {
    fn new(bytes: Vec<u8>) -> Self {
        Self { bytes }
    }
}

pub fn new_multi_buf(chunks: Vec<ffi::Chunk>) -> ffi::MultiBuf {
    ffi::MultiBuf::new(chunks)
}

impl ffi::MultiBuf {
    pub fn new(chunks: Vec<ffi::Chunk>) -> Self {
        Self { chunks, pos: 0 }
    }
}

pub fn next_chunk(buf: &mut ffi::MultiBuf) -> &[u8] {
    let next = buf.chunks.get(buf.pos);
    buf.pos += 1;
    next.map(|chunk| chunk.bytes.as_slice()).unwrap_or(&[])
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_next_chunk() {
        let mut buf = ffi::MultiBuf::new(vec![
            ffi::Chunk::new(vec![1, 2]),
            ffi::Chunk::new(vec![3, 4]),
        ]);
        let chunk1 = next_chunk(&mut buf);
        assert_eq!(chunk1, vec![1, 2]);

        let chunk2 = next_chunk(&mut buf);
        assert_eq!(chunk2, vec![3, 4]);

        let chunk3 = next_chunk(&mut buf);
        assert!(chunk3.is_empty());
    }
}
