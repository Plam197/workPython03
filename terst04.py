import math
a = float(input('ความกว้างของกล่อง (เมตร):'))
b = float(input('ความยาวของกล่อง (เมตร):'))
c = float(input('ความสูงของกล่อง (เมตร):'))
area=2*(a*c+b*c)
paint=math.ceil(area/5)
print('กล่องขนาดกล้าง {:.2f} เมตร ยาว {:.2f} เมตร สูง {:.2f} เมตร'.format(a,b,c))
print('ใช้จำนวนสี {} แกลลอน'.format(paint))
print(f'กล่องขนาดกล้าง {a:.2f} เมตร ยาว {b:.2f} เมตร สูง {c:.2f} เมตร')
print(f'ใช้จำนวนสี {paint} แกลลอน')
print('กล่องขนาดกล้าง',f' {a:.2f}','เมตร',' ยาว',f' {b:.2f}','เมตร','สูง',f' {c:.2f}','เมตร')
print('ใช้จำนวนสี','{paint:.2f}','แกลลอน')
print('กล่องขนาดกล้าง'+f' {a:.2f}'+'เมตร'+' ยาว'+f' {b:.2f}'+'เมตร'+'สูง'+f' {c:.2f}'+'เมตร')
print('ใช้จำนวนสี'+'{paint:.2f}'+'แกลลอน')
print('กล่องขนาดกล้าง %.2f เมตร ยาว %.2f เมตร สูง %.2f เมตร'%(a,b,c))
print('ใช้จำนวนสี %.2f แกลลอน'%(paint))