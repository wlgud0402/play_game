import turtle as t
#터틀이라는 것을 t로써 가져옴 이를통해 turtle이라고 통째로 안써도 됨
 
n = 60    # 원을 60번 그림
t.shape('turtle') #모양을 거북이로 변환시킴, 화살표등의 여러가지 있음

t.speed('fastest')      # 거북이 속도를 가장 빠르게 설정
for i in range(n):
    t.circle(120)       # 반지름이 120인 원을 그림
    t.right(360 / n)  

t.mainloop() #프로그래밍을 실행하고 바로 끝나는걸 방지함



# t.shape('turtle')
# t.speed('fastest')      # 거북이 속도를 가장 빠르게 설정
# for i in range(600):    # 300번 반복
#     t.forward(i)        # i만큼 앞으로 이동. 반복할 때마다 선이 길어짐
#     t.right(90)   

t.mainloop()