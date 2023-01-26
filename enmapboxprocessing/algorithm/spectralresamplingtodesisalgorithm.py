from enmapboxprocessing.algorithm.spectralresamplingbyresponsefunctionconvolutionalgorithmbase import \
    SpectralResamplingByResponseFunctionConvolutionAlgorithmBase
from enmapboxexternal.typeguard import typechecked


@typechecked
class SpectralResamplingToDesisAlgorithm(SpectralResamplingByResponseFunctionConvolutionAlgorithmBase):
    A_CODE = True

    def displayName(self) -> str:
        return 'Spectral resampling (to DESIS HSI)'

    def shortDescription(self) -> str:
        link = self.htmlLink('https://www.dlr.de/eoc/desktopdefault.aspx/tabid-13618/23664_read-54267/', 'DESIS')
        return super().shortDescription() + f'\nFor more information see the {link} mission website.'

    def code(self):
        from collections import OrderedDict

        responses = OrderedDict()
        wavelength = [402.0, 404.2, 406.8, 409.3, 411.8, 414.3, 416.9, 419.4, 422.0, 424.6, 427.3, 429.8, 432.4, 434.9,
                      437.5, 439.9, 442.5, 445.1, 447.8, 450.3, 452.9, 455.6, 458.2, 460.7, 463.3, 465.8, 468.3, 470.7,
                      473.4, 475.9, 478.5, 481.3, 483.8, 486.4, 489.0, 491.6, 494.0, 496.5, 499.2, 501.8, 504.3, 506.9,
                      509.5, 512.2, 514.7, 517.2, 519.6, 522.2, 524.7, 527.3, 529.7, 532.3, 534.9, 537.5, 540.2, 542.7,
                      545.2, 547.7, 550.3, 552.9, 555.5, 558.1, 560.6, 563.2, 565.8, 568.4, 571.0, 573.5, 576.1, 578.6,
                      581.1, 583.7, 586.3, 588.8, 591.3, 594.0, 596.6, 599.1, 601.6, 604.2, 606.8, 609.2, 611.8, 614.3,
                      616.9, 619.5, 622.1, 624.7, 627.2, 629.7, 632.2, 634.7, 637.2, 639.8, 642.3, 644.9, 647.5, 650.0,
                      652.6, 655.2, 657.7, 660.2, 662.8, 665.3, 667.9, 670.5, 673.1, 675.8, 678.4, 680.9, 683.5, 685.9,
                      688.4, 690.9, 693.5, 696.2, 698.8, 701.5, 703.9, 706.7, 709.4, 711.8, 714.0, 716.4, 718.9, 721.6,
                      724.2, 726.9, 729.4, 732.1, 734.4, 736.9, 739.5, 742.0, 744.5, 747.2, 749.7, 752.3, 755.2, 757.7,
                      760.3, 763.0, 765.0, 767.5, 770.3, 772.7, 775.4, 778.0, 780.5, 783.0, 785.6, 788.2, 790.6, 793.1,
                      795.9, 798.4, 801.2, 804.0, 806.7, 809.1, 811.7, 814.3, 816.9, 819.8, 822.8, 824.2, 827.2, 829.2,
                      832.2, 834.9, 836.7, 840.1, 842.0, 844.7, 847.7, 850.0, 852.4, 855.4, 857.9, 860.3, 862.9, 865.4,
                      868.0, 870.6, 873.2, 875.8, 878.8, 881.5, 883.1, 885.3, 888.1, 890.9, 894.1, 896.0, 898.3, 901.2,
                      903.7, 906.0, 908.7, 911.6, 914.8, 916.6, 918.4, 921.0, 923.9, 927.1, 929.6, 931.9, 934.5, 937.3,
                      939.4, 942.0, 944.7, 947.3, 949.6, 951.9, 954.2, 957.3, 959.6, 962.3, 965.5, 968.1, 970.4, 972.9,
                      976.0, 978.7, 980.0, 981.9, 984.8, 988.9, 991.6, 993.1, 995.6, 997.9, 999.5]
        fwhm = [2.4, 3.6, 3.8, 3.8, 3.6, 3.8, 3.4, 3.4, 3.6, 3.6, 3.4, 3.4, 3.2, 3.2, 3.0, 3.2, 3.4, 3.2, 3.4, 3.4, 3.4,
                3.6, 3.4, 3.4, 3.2, 3.2, 3.4, 3.2, 3.2, 3.4, 3.4, 3.4, 3.2, 3.2, 3.2, 3.2, 3.2, 3.2, 3.4, 3.4, 3.4, 3.6,
                3.6, 3.4, 3.4, 3.4, 3.4, 3.4, 3.4, 3.6, 3.4, 3.4, 3.6, 3.6, 3.4, 3.4, 3.6, 3.6, 3.6, 3.4, 3.4, 3.4, 3.6,
                3.6, 3.6, 3.6, 3.6, 3.6, 3.4, 3.4, 3.4, 3.4, 3.6, 3.6, 3.6, 3.6, 3.6, 3.4, 3.6, 3.6, 3.4, 3.4, 3.6, 3.4,
                3.4, 3.4, 3.4, 3.4, 3.4, 3.4, 3.2, 3.4, 3.4, 3.4, 3.4, 3.6, 3.6, 3.4, 3.6, 3.4, 3.4, 3.4, 3.4, 3.4, 3.4,
                3.4, 3.6, 3.6, 3.4, 3.4, 3.4, 3.4, 3.2, 3.4, 3.4, 3.4, 3.6, 3.6, 3.8, 3.6, 3.6, 4.0, 4.0, 3.8, 3.4, 3.4,
                3.6, 3.4, 3.4, 3.2, 3.2, 3.4, 3.4, 3.2, 3.4, 3.4, 3.4, 3.4, 3.6, 3.4, 3.4, 3.6, 3.0, 3.4, 3.4, 3.4, 3.4,
                3.6, 3.2, 3.4, 3.2, 3.4, 3.2, 3.4, 3.4, 3.4, 3.2, 3.0, 3.0, 3.0, 3.0, 3.0, 3.2, 3.6, 3.2, 3.0, 3.6, 2.8,
                3.6, 2.6, 3.0, 3.4, 2.8, 3.4, 3.4, 3.0, 3.2, 3.2, 3.2, 3.0, 3.4, 3.2, 3.4, 3.4, 3.4, 3.6, 4.0, 3.0, 3.0,
                3.4, 3.6, 3.6, 3.6, 3.2, 3.2, 3.6, 3.6, 3.0, 4.0, 4.0, 3.8, 3.0, 3.6, 4.0, 3.6, 3.4, 3.4, 3.2, 3.8, 3.4,
                3.2, 3.8, 3.6, 3.6, 3.6, 3.0, 3.6, 3.4, 3.4, 3.4, 3.6, 3.8, 3.6, 3.4, 4.8, 3.6, 2.8, 4.0, 6.6, 4.2, 3.4,
                3.0, 3.4, 3.4, 3.0]
        for w, f in zip(wavelength, fwhm):
            responses[w] = f
        return responses
