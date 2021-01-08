# Copyright 2013-2021 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: MIT


from spack import *


class OneapiTestVirtual(Package):
    """Test oneapi package for spack."""

    homepage = "https://github.com/rscohn2/oneapi-spack-tests"
    url = "https://github.com/rscohn2/oneapi-spack-tests/tarball/main"

    maintainers = ["rscohn2"]

    variant(
        "sycl",
        default=True,
        description="Include tests that depend on SYCL support in the compiler",
    )

    version(
        "0.1",
        sha256="0eaea9c9c33b5d69c1a12044481bd38cc35f967a533b26a0d8c21c4c4d17249b",
    )

    depends_on("hdf5")
    depends_on("intel-oneapi-dal")
    depends_on("tbb")
    depends_on("mkl")
    depends_on("mpi")

    def install(self, spec, prefix):
        sycl = "+sycl" in self.spec
        sycl_samples = "X=1" if sycl else "SYCL_SAMPLES="
        make("-C", "samples", sycl_samples)
        make(
            "-C",
            "samples",
            "install",
            "PREFIX={0}".format(prefix),
            sycl_samples,
        )
