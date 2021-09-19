import os
#tạo bảng nhân viên
#mã nhân viên, tên nhân viên, số công(reset vào ngày 1 hàng tháng), 
class salarymen: 
    def __init__(self, id, name, age, workcount):
        self.id = id
        self.name = name
        self.age = age
        self.salary = 10000000
        self.workcount = workcount
class worker(salarymen):
    def __init__(self, id, name, age, workcount, product):
        super().__init__(id, name, age, workcount)
        self.coef =  1.5
        #sản phẩm vượt yêu cầu sẽ được thưởng thêm
        self.product = product
    #tính lương
    def salarypay(self):
        if self.product > 300 :
            extra = (self.product - 300)*20000
        else: extra = 0
        return self.salary * self.coef - ((30 - self.workcount)*50000) + extra 

class hrstaff(salarymen):
    def __init__(self, id, name, age, workcount):
        super().__init__(id, name, age, workcount)
        self.coef = 2.0
    def salarypay(self):
        return self.salary * self.coef

class counter(salarymen):
    def __init__(self, id, name, age, workcount):
        super().__init__(id, name, age, workcount)
        self.coef = 1.9
    def salarypay(self):
        return self.salary * self.coef

list = []
# Giao diện chọn
while True:
    print("\n\n\nNhập lựa chọn: \n")
    print("\n1. Thêm mới tài khoản nhân viên")#Bao gồm nút tính lương
    print("\n2. Xóa tài khoản nhân viên")
    print("\n3. Sửa thông tin tài khoản")
    print("\n0. Thoát")
    choice = int(input("\nNhập: "))
    os.system('cls')
    if choice in [0,1,2,3,4]:
        if choice == 1 :
            role = input("\n\n Nhập chức vụ làm việc (công nhân(worker), nhân sự(HR), kế toán(counter)): ")
            if role.lower() in ["cong nhan", "công nhân", "worker"] :
                    id = input("\n\nNhập ID nhân viên: ")
                    name = input("\n\n Nhập tên nhân viên: ")
                    age = int(input("\n\n Nhập tuổi: "))
                    work = int(input("\n\n Nhập công tháng này: "))
                    product = int(input("\n\n Nhập số sản phẩm: "))
                    person = worker(id,name, age, work, product)
                    list.append(person)
                    del person
            elif role.lower() in ["nhan su", "nhân sự", "hr"] :
                    id = input("\n\nNhập ID nhân viên: ")
                    name = input("\n\n Nhập tên nhân viên: ")
                    age = int(input("\n\n Nhập tuổi: "))
                    work = int(input("\n\n Nhập công tháng này: "))
                    person = hrstaff(id,name,age,work)
                    list.append(person)
                    del person
            elif role.lower() in ["counter", "ke toan", "kế toán"] :
                    id = input("\n\nNhập ID nhân viên: ")
                    name = input("\n\n Nhập tên nhân viên: ")
                    age = int(input("\n\n Nhập tuổi: "))
                    work = int(input("\n\n Nhập công tháng này: "))
                    person = counter(id,name,age,work)
                    list.append(person)
                    del person
            else: print("\nVui lòng nhập đúng!")
            os.system('cls')
        if choice == 2 :
            delete = input("\n\n Nhập mã nhân viên cần xóa: ")
            for x in list :
                if x.id == delete :
                    list.remove(x)
            os.system('cls')
        if choice == 3:
            change = input("/n Nhập mã nhân viên cần thay đổi: ")
            name = input("\n\n Nhập tên nhân viên: ")
            age = int(input("\n\n Nhập tuổi: "))
            work = int(input("\n\n Nhập công tháng này: "))
            product = int(input("\n\n Nhập số sản phẩm(bỏ qua nếu không phải công nhân): "))
            for i in list:
                if i.id == change:
                    i.name = name
                    i.age =  age
                    i.workcount = work
                    if hasattr(i,"product"):
                        i.product = product
                    else: print("Nhân viên này không phải công nhân!")
            else: print("không tìm thấy giá trị")
            os.system('cls')
        if choice == 4 :
            for i in list: 
                print("\n\n\n Mã nhân viên: ", i.id)
                print("\n Tên nhân viên: ", i.name)
                print("\n Tuổi: {}".format(i.age))
                print("\n Số công: {}".format(i.workcount))
                if hasattr(i,"product"):
                    print("\n Số sản phẩm tạo vượt: {}".format(i.product))
    else:
        print("\n\nYêu cầu không hợp lệ!")
        os.system('cls')



