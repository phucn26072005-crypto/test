import heapq
import time

def visualize_grid(grid, path=None, current=None):
    """Hiển thị grid với minh họa trực quan"""
    symbols = {
        0: '⬜',  # Đường thông
        1: '🚧',  # Kẹt xe
        'start': '🏠',  # Điểm bắt đầu
        'goal': '🏫',  # Điểm kết thúc
        'path': '🟢',  # Đường đi
        'current': '🔴'  # Vị trí hiện tại
    }
    
    for i in range(len(grid)):                          # duyệt từng hàng trong bản đồ (grid)

        for j in range(len(grid[0])):                   # duyệt từng cột trong mỗi hàng 

            pos = (i, j)                                # tạo ra một tọa độ (hàng, cột)

            if pos == current:                          # nếu ô này đúng là vị trí hiện tại


                print(symbols['current'], end=' ')      
            elif path and pos in path:                  # nếu có đường đi (path) và ô này nằm trên đường đi
                if pos == path[0]:                      # nếu là điểm bắt đầu
                    print(symbols['start'], end=' ')
                elif pos == path[-1]:                   # nếu là điểm đích
                    print(symbols['goal'], end=' ')
                else:                                   # còn lại thì là ô nằm trên đường đi
                    print(symbols['path'], end=' ')     
            else:                                       # nếu không phải vị trí hiện tại hay đường đi
                print(symbols[grid[i][j]], end=' ')
        print()

#Heuristic trong A*-----------------------------------------------------
def astar(grid, start, goal):
    def heuristic(a, b):
        # Khoảng cách Manhattan (tạm coi là thời gian đi bộ/xe)
        return abs(a[0] - b[0]) + abs(a[1] - b[1]) #vidu : nếu bạn ở (2,3) và trường ở (5,7) → còn ít nhất |2-5| + |3-7| = 3 + 4 = 7 bước nữa.
    
    open_set = []
    heapq.heappush(open_set, (0, start))
    
    came_from = {}
    g_score = {start: 0}
    f_score = {start: heuristic(start, goal)}
    
    directions = [(1,0), (-1,0), (0,1), (0,-1)]
    step = 0
    
    
    print("=== BẮT ĐẦU TÌM ĐƯỜNG ĐẾN ĐẠI HỌC CÔNG THƯƠNG ===")
    print(f"Điểm xuất phát: {start} (🏠 Nhà bạn)")
    print(f"Điểm đến: {goal} (🏫 Trường ĐH Công Thương)")
    print("\nBản đồ ban đầu:")
    visualize_grid(grid)
    
    while open_set:
        current = heapq.heappop(open_set)[1]
        
        # In thông tin bước đi
        print(f"\n🧭 BƯỚC {step}: Đang tại {current}")
        print(f"   ⏱️  Đã đi: {g_score[current]} phút")
        print(f"   📍 Ước tính còn: {heuristic(current, goal)} phút")
        print(f"   🎯 Tổng dự kiến: {f_score[current]} phút")
        print(f"\n")
        
        # Hiển thị grid với vị trí hiện tại
        visualize_grid(grid, current=current)
        time.sleep(0)
        
        print("\n")

        if current == goal:
            print("\n🎉 CHÚC MỪNG! Đã tìm được đường đến Đại học Công Thương!")
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            path.append(start)
            path = path[::-1]
            
            print("\n🗺️ Lộ trình hoàn chỉnh:")
            visualize_grid(grid, path=path)
            return path
        
        #duyệt ô hàng xóm
        for dx, dy in directions:
            neighbor = (current[0] + dx, current[1] + dy)
            
            # Kiểm tra biên
            if (0 <= neighbor[0] < len(grid) and
                0 <= neighbor[1] < len(grid[0])):
                
                # Kiểm tra kẹt xe
                if grid[neighbor[0]][neighbor[1]] == 1:
                    print(f"   ❌ Đường {neighbor} đang kẹt xe (🚧), không đi được")
                    continue
                
                #chi phí của current + 1
                tentative_g = g_score[current] + 1
                
                #update nếu có đường đi ngắn hơn với chi phí ít hơn
                if neighbor not in g_score or tentative_g < g_score[neighbor]:
                    came_from[neighbor] = current
                    g_score[neighbor] = tentative_g
                    f_score[neighbor] = tentative_g + heuristic(neighbor, goal)
                    heapq.heappush(open_set, (f_score[neighbor], neighbor))
                    print(f"   ✅ Có thể đi đến {neighbor}, tổng thời gian dự kiến: {f_score[neighbor]} phút")
        
        step += 1
    
    print("\n😢 Rất tiếc, không tìm thấy đường đến trường...")
    return None


# -------------------------------------------------------------
# 0 = đường thông, 1 = kẹt xe
grid = [
    [0, 0, 0, 0, 0],
    [1, 1, 0, 1, 0],
    [0, 0, 0, 1, 0],
    [0, 1, 1, 1, 0],
    [0, 0, 0, 0, 0]
]

start = (0, 0)   # nhà bạn
goal = (4, 4)    # Đại học Công Thương
# -------------------------------------------------------------
print("=" * 50)
path = astar(grid, start, goal)

print("\n=== KẾT QUẢ CUỐI CÙNG ===")
if path:
    print(f"Lộ trình tối ưu: {path}")
    print(f"Tổng thời gian di chuyển: {len(path)-1} phút")
else:
    print("Không tìm thấy đường đi phù hợp")
print("=" * 50)