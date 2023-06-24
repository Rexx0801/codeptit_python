class GiaoVien:
    def __init__(self, STT, Ten, MaXetTuyen, DiemTinHoc, DiemChuyenMon):
        if len(STT) == 1: self.STT = 'GV0' + STT
        else: self.STT = 'GV' + STT
        self.Ten = Ten
        self.MaXetTuyen = MaXetTuyen
        self.DiemTinHoc = DiemTinHoc
        self.DiemChuyenMon = DiemChuyenMon
    def mon(self):
        if self.MaXetTuyen[0] == 'A': return 'TOAN'
        elif self.MaXetTuyen[0] == 'B': return 'LY'
        else: return 'HOA'
    def uuTien(self):
        if self.MaXetTuyen[1] == '1': return 2.0
        elif self.MaXetTuyen[1] == '2': return 1.5
        elif self.MaXetTuyen[1] == '3': return 1.0
        else: return 0.0
    def diem(self):
        return '%.1f' % (self.DiemTinHoc * 2 + self.DiemChuyenMon + self.uuTien())
    def xepHang(self):
        if float(self.diem()) >= 18: return 'TRUNG TUYEN'
        else: return 'LOAI'
    def __str__(self):
        return f'{self.STT} {self.Ten} {self.mon()} {self.diem()} {self.xepHang()}'
if __name__ == '__main__':
    n = int(input())
    a = []
    for i in range(1, n + 1):
        a.append(GiaoVien(str(i), input(), input(), float(input()), float(input())))
    a.sort(reverse=True, key= lambda x : x.diem())
    for ele in a:
        print(ele)    