# Hướng Dẫn Đóng Góp (Contributing Guide)

Chào mừng các biên tập viên, thiết kế và lập trình viên tham gia hoàn thiện bộ công cụ **Znews Editorial Studio**!

---

## 📌 Nguyên Tắc Đóng Góp
1. **Ưu tiên sự đơn giản & Client-side**: Mọi tính năng mới không được làm phức tạp hóa quy trình xuất bản của phóng viên. Công cụ phải chạy trực tiếp trên trình duyệt mà không cần cài thêm phần mềm hỗ trợ.
2. **Tuân thủ quy chuẩn CMS Znews (Ad-Safe)**: Mọi đoạn mã sinh ra bắt buộc phải bảo toàn 100% hiển thị các banner quảng cáo và tương thích với CSS của tòa soạn (Xem chi tiết tại [docs/CMS_GUIDELINES.md](./docs/CMS_GUIDELINES.md)).
3. **Kiểm tra đa nền tảng**: Luôn kiểm thử giao diện trên cả màn hình di động (iOS Safari, Android Chrome) và máy tính (Chrome, Edge, Safari).

---

## 🛠️ Quy Trình Gửi Đóng Góp (Pull Request)

1. **Fork hoặc tạo nhánh mới** từ nhánh `main`:
   ```bash
   git checkout -b feature/ten-tinh-nang-moi
   ```
2. **Thực hiện thay đổi** và kiểm thử cẩn thận trên môi trường cục bộ (`python3 -m http.server 8080`).
3. **Commit** theo định dạng chuẩn Conventional Commits:
   - `feat: ...` khi thêm công cụ hoặc tính năng mới.
   - `fix: ...` khi sửa lỗi hiển thị hoặc xử lý sự cố CMS.
   - `docs: ...` khi cập nhật tài liệu hướng dẫn.
4. **Đẩy lên GitHub** và tạo Pull Request để ban quản trị duyệt nhập vào nhánh `main`.
