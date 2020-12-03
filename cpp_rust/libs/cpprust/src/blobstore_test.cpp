#include "cpprust/blobstore.hpp"

#include "gtest/gtest.h"

namespace cpprust::tests {

TEST(CppRustTests, TestNewBlobStoreClient) {
  const auto blobstore = new_blobstore_client();
  EXPECT_TRUE(blobstore);
}

}  // namespace cpprust::tests
