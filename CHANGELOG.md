# Nhật Ký Thay Đổi & Lịch Sử Phiên Bản (Changelog)

Toàn bộ các cập nhật quan trọng của dự án **Znews Editorial Studio** được ghi nhận chi tiết tại đây.

---

## [2.4.0] - 2026-10-04

### ⚖️ Ra mắt công cụ bài so sánh đối chiếu (Comparison Story Tool)
- **Thiết kế chuyên sâu cho bài viết so sánh đa chiều**:
  - Hỗ trợ bài viết có nhiều mục nhỏ (sections), mỗi mục gồm 2 hình ảnh đại diện cho hai góc nhìn (ví dụ: "Đánh đổi" và "Lợi ích", "Trước" và "Sau", "Lựa chọn A" và "Lựa chọn B") cùng 2 phần mô tả phân tích chuyên sâu.
- **Thanh trượt ảnh kép kiểu iPhone (iOS slide switcher)**:
  - Tích hợp đồng thời vạch chia trượt trực tiếp trên ảnh (split handle) và thanh trượt viên thuốc kiểu iOS (iOS pill slider) phía dưới ảnh.
  - Hiệu ứng chữ nhấp nháy phát sáng (shimmer animation) gợi ý hướng trượt: *"Trượt để xem lợi ích ›››"* hoặc *"‹‹‹ Trượt để xem đánh đổi"*.
  - Nút bấm chọn nhanh (tab badges): Người đọc có thể bấm trực tiếp vào nhãn "Đánh đổi" hoặc "Lợi ích" để trượt chuyển cảnh mượt mà.
- **Ma trận 2 cột văn bản cân đối (Balanced Text Matrix)**:
  - Khối văn bản 2 cột nằm ngay dưới ảnh, hai thẻ (Card A và Card B) tự động kéo dãn bằng nhau (`align-items: stretch`).
  - Cho phép người viết nhập 1 hoặc 2–3 đoạn văn bản phân tích dài cho mỗi bên mà vẫn giữ tỷ lệ 50/50 hoàn hảo trên desktop và tự động xếp chồng thông minh trên di động.
  - Đồng bộ độ sáng tương tác theo vị trí thanh trượt: bên được chọn sẽ sáng rõ, bên đối lập mờ nhẹ, ở giữa thì cả hai cùng nổi bật.
- **Tương thích toàn diện CMS Znews & bảo toàn quảng cáo (Ad-Safe)**:
  - Sử dụng namespace độc lập `.zac#zacCompare` ngăn ngừa xung đột giao diện toàn trang.
  - Tự động triệt tiêu lỗi tràn viền bleed (`--zc-bleed: 0px`) trên bố cục `layout-special` và `mode-bleed`, chống hiện tượng mất chữ hoặc lệch ảnh.
  - Thang độ phân giải ảnh retina thích ứng `zcFixSize` (từ 360px đến 1920px) cho toàn bộ ảnh trên Znews CDN.
- **Tích hợp vào hệ sinh thái Studio Hub**:
  - Thêm thẻ công cụ trên trang chủ `index.html` với đầy đủ bộ lọc, tìm kiếm và bộ chọn nhanh `#toolSwitcher`.
  - Cập nhật số liệu thống kê (8 công cụ chuyên dụng) và sổ tay hướng dẫn chi tiết `docs/TOOL_MANUAL.md`.

---

## [2.3.1] - 2026-10-04

### 🎯 Sửa lỗi căn giữa ảnh đơn trong bài phỏng vấn (Interview Tool)
- **Khắc phục lỗi ảnh đơn bị lệch trái trên chế độ tràn viền (`mode-bleed`)**:
  - Đổi quy tắc `.zac#zacInterview.mode-bleed .zi-wide` từ `margin-left: 0; margin-right: 0;` sang `margin-left: auto; margin-right: auto;`.
  - Bổ sung `margin-left: auto; margin-right: auto;` cho `.zi-insert.zi-wide` để đảm bảo 3 khối ảnh chèn (`.zi-insert.zi-photo.zi-wide`) và dải số liệu luôn được căn giữa hoàn hảo trong khung nhìn bài viết rộng 1268px - 1629px.

---

## [2.3.0] - 2026-10-03

### 🎙️ Tích hợp công cụ phỏng vấn (Interview Tool) & vá lỗi tràn viền layout-special
- **Khắc phục triệt để lỗi tràn mép 130px trên bố cục `layout-special` của CMS**:
  - Tự động tắt biến margin âm (`--bleed: 0px`) khi bài phỏng vấn đặt trong bố cục `layout-special` hoặc có lớp `mode-bleed`, loại bỏ hoàn toàn lỗi đẩy 7 khối phần tử ra ngoài viewport làm mất chữ đầu tiêu đề/sapo và tràn ảnh chèn.
  - Xử lý dứt điểm trường hợp 3 ảnh chèn (`.zi-insert.zi-photo.zi-wide`) bị tràn khi áp dụng `mode-bleed` bằng cách đặt lại margin 0 an toàn.
  - Căn giữa và thu gọn cột chữ (`.zi-intro`, `.zi-qa`, `.zi-toc`, `.zi-quote`, `.zi-book`, `.zi-endnav`) với độ rộng chuẩn `max-width: 760px; margin-inline: auto; padding-inline: 16px;`, giúp bài viết không bị dạt sang mép trái màn hình lớn (1629px) và dễ đọc tối ưu.
  - Xuất trực tiếp thẻ `<article class="zac mode-bleed" id="zacInterview">` không phụ thuộc script đánh thức `zacWake`, đảm bảo hiển thị đúng 100% ngay cả khi CMS lọc thẻ `<script>`.
- **Tích hợp Interview Tool vào Studio Hub (`index.html`)**:
  - Thêm thẻ công cụ Phỏng vấn vào danh mục Dàn trang và layout trên trang chủ Studio.
  - Cập nhật bộ chọn chuyển đổi nhanh (`#toolSwitcher`) trong khung làm việc đa nhiệm.
  - Bổ sung tài liệu hướng dẫn chi tiết vào `docs/TOOL_MANUAL.md` và `README.md`.

---

## [2.2.0] - 2026-09-27

### 🌟 Nâng cấp công cụ dựng bài ảnh (Photo Essay v3)
- **Thang phân giải thích ứng thông minh (Responsive Image Ladder)**:
  - Tích hợp thang phân giải [360, 480, 660, 860, 960, 1024, 1200, 1920] qua các hàm `zpPick`, `zpSized` và `zpFixSize`.
  - Tự động phát hiện khi CMS phục vụ ảnh thumbnail nhỏ (`w210`) và tự động nâng cấp độ phân giải sắc nét theo màn hình retina.
- **Cơ chế chống méo tỷ lệ ảnh (Ratio Drift Guard - `zpCheckRatio`)**:
  - Tự động phát hiện sai lệch tỷ lệ khung hình giữa ảnh thật và thuộc tính khai báo nếu lệch trên 5%, gắn cờ `zpv={w}x{h}` hoặc hoàn nguyên ảnh gốc để bảo vệ bố cục.
- **Lightbox zoom độ phân giải cao (High-Res Lightbox)**:
  - Tự động tải độ phân giải tối ưu (lên tới 1920px) khi mở phóng to trong Lightbox, mang lại chất lượng hiển thị sắc sảo trên màn hình 4K và Retina.
- **Cơ chế fallback đa tầng (`data-zp-orig`)**:
  - Ghi nhớ URL ảnh gốc, tự động hồi phục về ảnh gốc nếu bất kỳ link ảnh resize CDN nào bị lỗi mạng hoặc 404.

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
