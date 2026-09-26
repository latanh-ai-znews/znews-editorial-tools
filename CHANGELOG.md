# Nhật Ký Thay Đổi & Lịch Sử Phiên Bản (Changelog)

Toàn bộ các cập nhật quan trọng của dự án **Znews Editorial Studio** được ghi nhận chi tiết tại đây.

---

## [2.1.0] - 2026-09-26

### 🚀 Cập nhật công cụ dựng bài ảnh (Photo Essay v2)
- **Tự động đồng bộ breadcrumb chuyên mục**:
  - Tự động trích xuất breadcrumb chuyên mục từ CMS Znews hiển thị ở đầu bài và khối điều hướng chân trang (`zp-endnav`), loại bỏ việc phải nhập tay.
- **Cơ chế fallback ảnh CDN Znews tự động (`zpInitImgFallback`)**:
  - Tự động bắt lỗi tải ảnh và chuyển đổi sang URL độ phân giải cao `photo.znews.vn/w1920/Uploaded/` nếu ảnh gốc bị lỗi CDN hoặc thiếu srcset.
- **Bố cục lưới ảnh chống giật layout**:
  - Áp dụng kỹ thuật padding-bottom theo tỷ lệ khung hình thật (`zp-pb-` và `zp-gw-`), triệt tiêu hiện tượng Cumulative Layout Shift (CLS) khi tải trang.
- **Nâng cấp trình xem Lightbox toàn màn hình**:
  - Dynamic caption layout, click outside detection thông minh, vuốt chuyển ảnh mượt mà trên màn hình cảm ứng di động.

---

## [2.0.0] - 2026-09-25

### ✨ Điểm Mới & Nâng Cấp Toàn Diện (Major Release)
- **Znews Editorial Studio Hub (`index.html`)**:
  - Xây dựng cổng trung tâm điều khiển tập trung cho toàn bộ 6 công cụ và cẩm nang kỹ thuật.
  - Tích hợp không gian làm việc Studio đa nhiệm (In-App Workspace): chuyển đổi tức thì giữa các công cụ qua thanh điều hướng tiện lợi.
  - Hệ thống tìm kiếm theo thời gian thực (phím tắt `/`) và phân loại theo chuyên mục.
  - Hỗ trợ chế độ giao diện Sáng / Tối (phím tắt `D`) lưu trữ qua `localStorage`.
- **Cẩm Nang Kỹ Thuật Số Hóa (`guide.html`)**:
  - Chuyển đổi toàn bộ quy chuẩn CMS Znews sang giao diện đọc trực quan, có mục lục sticky và nút sao chép mã nguồn nhanh.
- **Triển khai Trực tuyến Toàn cầu (GitHub Pages)**:
  - Tự động hóa quy trình xuất bản web lên GitHub Pages tại địa chỉ: `https://latanh-ai-znews.github.io/znews-editorial-tools/`.
  - Cho phép truy cập và sử dụng từ bất kỳ thiết bị nào (điện thoại, máy tính bảng, máy tính cá nhân).
- **Bộ Tài Liệu Kỹ Thuật Chuyên Nghiệp (`docs/`)**:
  - `docs/TOOL_MANUAL.md`: Sổ tay hướng dẫn chi tiết 6 công cụ.
  - `docs/CMS_GUIDELINES.md`: Quy chuẩn kỹ thuật Ad-Safe và bố cục CMS Znews.
  - `docs/ARCHITECTURE.md`: Kiến trúc kỹ thuật, client-side model và namespace CSS.
  - `docs/DEVELOPER_GUIDE.md`: Cẩm nang mở rộng, thêm công cụ và quy trình deploy.
  - `docs/TROUBLESHOOTING.md`: Hướng dẫn xử lý sự cố & các lỗi thường gặp.

---

## [1.0.0] - 2026-08-10 đến 2026-09-25

### 📦 Phát Hành Các Công Cụ Đơn Lẻ Ban Đầu
- **Znews Magazine Layouts Generator (v10.13)**: Hỗ trợ import mã nguồn bài viết, đa dạng layout magazine, hiệu ứng parallax cuộn.
- **Dựng bài no side-bar (Ad-Safe)**: Giải pháp bảo vệ hiển thị 3 vùng quảng cáo, nhận diện quote và chuỗi ảnh.
- **Công cụ dựng bài ảnh (Photo Essay)**: Bố cục full-bleed, ảnh đôi/ba, chuyển đổi bài ảnh cũ.
- **Znews Thumb Định Dạng Đặc Biệt**: Đóng logo chính thức của Znews, xuất ảnh chuẩn 900×600 px.
- **Trình tạo bài viết sách (CMS Books)**: Hỗ trợ box sách, tự động chuẩn hoá dấu em-dash.
- **Công cụ tạo Carousel ảnh**: Khối slide ảnh cảm ứng mượt mà nhúng trong bài.
