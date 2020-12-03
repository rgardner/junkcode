#include <iostream>

#include "cpprust/cpprust.hpp"
#include "rust/cxx.hpp"

int main() {
  std::cout << "Creating blobstore...\n";
  auto client = cpprust::new_blobstore_client();

  // Upload a blob.
  auto chunks = rust::Vec<cpprust::Chunk>{};
  chunks.emplace_back(cpprust::Chunk{{'a', 'b', 'c'}});
  chunks.emplace_back(cpprust::Chunk{{'1', '2', '3'}});
  auto buf = cpprust::new_multi_buf(std::move(chunks));
  const auto blob_id = client->put(buf);
  std::cout << "blob_id: " << blob_id << std::endl;

  // Add a tag.
  client->tag(blob_id, "rust");
  client->tag(blob_id, "c++");

  // Read back the tags.
  const auto metadata = client->metadata(blob_id);
  std::cout << "tags: [";
  for (auto it = metadata.tags.cbegin(); it != metadata.tags.end(); ++it) {
    if (it != metadata.tags.cbegin()) {
      std::cout << " ";
    }
    std::cout << *it;
  }
  std::cout << "]" << std::endl;

  return 0;
}
