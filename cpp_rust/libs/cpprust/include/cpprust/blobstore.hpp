#pragma once

#include <memory>

#include "rust/cxx.hpp"

namespace cpprust {

struct MultiBuf;
struct BlobMetadata;

class BlobstoreClient {
 public:
  BlobstoreClient();

  std::uint64_t put(MultiBuf& buf) const;
  void tag(std::uint64_t blobid, rust::Str tag) const;
  BlobMetadata metadata(std::uint64_t blobid) const;

 private:
  class impl;
  std::shared_ptr<impl> impl_;
};

std::unique_ptr<BlobstoreClient> new_blobstore_client();

}  // namespace cpprust
