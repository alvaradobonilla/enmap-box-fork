import numpy as np

from enmapboxprocessing.algorithm.importprismal2calgorithm import ImportPrismaL2CAlgorithm
from enmapboxprocessing.algorithm.testcase import TestCase
from enmapboxprocessing.rasterreader import RasterReader
from enmapboxtestdata import sensorProductsRoot, SensorProducts


class TestImportPrismaL2CAlgorithm(TestCase):

    def test(self):
        if sensorProductsRoot() is None:
            return

        alg = ImportPrismaL2CAlgorithm()
        parameters = {
            alg.P_FILE: SensorProducts.Prisma.L2C,
            alg.P_OUTPUT_SPECTRAL_CUBE: self.filename('prismaL2C_SPECTRAL.tif'),
            alg.P_OUTPUT_SPECTRAL_GEOLOCATION: self.filename('prismaL2C_SPECTRAL_GEOLOCATION.vrt'),
            alg.P_OUTPUT_SPECTRAL_GEOMETRIC: self.filename('prismaL2C_SPECTRAL_GEOMETRIC.vrt'),
            alg.P_OUTPUT_SPECTRAL_ERROR: self.filename('prismaL2C_SPECTRAL_ERROR.tif'),
            alg.P_OUTPUT_PAN_CUBE: self.filename('prismaL2C_PAN.vrt'),
            alg.P_OUTPUT_PAN_GEOLOCATION: self.filename('prismaL2C_PAN_GEOLOCATION.vrt'),
            alg.P_OUTPUT_PAN_ERROR: self.filename('prismaL2C_PAN_ERROR.vrt'),
        }
        result = self.runalg(alg, parameters)
        self.assertEqual(234, RasterReader(result[alg.P_OUTPUT_SPECTRAL_CUBE]).bandCount())
        self.assertAlmostEqual(0.101, np.mean(RasterReader(result[alg.P_OUTPUT_SPECTRAL_CUBE]).array()), 3)

        self.assertEqual(2, RasterReader(result[alg.P_OUTPUT_SPECTRAL_GEOLOCATION]).bandCount())
        self.assertAlmostEqual(32.920, np.mean(RasterReader(result[alg.P_OUTPUT_SPECTRAL_GEOLOCATION]).array()), 3)

        self.assertEqual(3, RasterReader(result[alg.P_OUTPUT_SPECTRAL_GEOMETRIC]).bandCount())
        self.assertAlmostEqual(48.745, np.mean(RasterReader(result[alg.P_OUTPUT_SPECTRAL_GEOMETRIC]).array()), 3)

        self.assertEqual(234, RasterReader(result[alg.P_OUTPUT_SPECTRAL_ERROR]).bandCount())
        self.assertAlmostEqual(0.049, np.mean(RasterReader(result[alg.P_OUTPUT_SPECTRAL_ERROR]).array()), 3)

        self.assertEqual(1, RasterReader(result[alg.P_OUTPUT_PAN_CUBE]).bandCount())
        self.assertAlmostEqual(0.338, np.mean(RasterReader(result[alg.P_OUTPUT_PAN_CUBE]).array()), 3)

        self.assertEqual(2, RasterReader(result[alg.P_OUTPUT_PAN_GEOLOCATION]).bandCount())
        self.assertAlmostEqual(32.920, np.mean(RasterReader(result[alg.P_OUTPUT_PAN_GEOLOCATION]).array()), 3)

        self.assertEqual(1, RasterReader(result[alg.P_OUTPUT_PAN_ERROR]).bandCount())
        self.assertAlmostEqual(0.005, np.mean(RasterReader(result[alg.P_OUTPUT_PAN_ERROR]).array()), 3)
