# Studio biên tập Znews — Bộ công cụ dàn trang và xuất bản báo chí

[![GitHub Pages](https://img.shields.io/badge/GitHub%20Pages-Live%20Website-success?style=for-the-badge&logo=github)](https://latanh-ai-znews.github.io/znews-editorial-tools/)
[![Version](https://img.shields.io/badge/Version-2.1.0-blue?style=for-the-badge)](CHANGELOG.md)
[![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)](LICENSE)
[![Platform](https://img.shields.io/badge/Platform-Web%20%7C%20Mobile%20%7C%20Desktop-orange?style=for-the-badge)](index.html)

Hệ thống công cụ chuyên nghiệp phục vụ công tác dàn trang magazine, phóng sự ảnh (photo essay), đóng khung ảnh đại diện chuẩn 900×600, tạo slide ảnh (carousel) và soạn thảo bài viết chuyên đề chuẩn CMS báo điện tử **Znews**.

Được xây dựng theo mô hình **100% client-side**, hoạt động trực tiếp trên trình duyệt, không cần máy chủ, đảm bảo bảo mật nội dung tuyệt đối và tương thích mượt mà trên mọi thiết bị.

---

## 🌐 Đường dẫn truy cập trực tuyến

* 🔗 **Website công cụ trực tuyến (GitHub Pages):**  
  👉 **[https://latanh-ai-znews.github.io/znews-editorial-tools/](https://latanh-ai-znews.github.io/znews-editorial-tools/)**
* 📁 **Kho lưu trữ mã nguồn (GitHub Repository):**  
  👉 **[https://github.com/latanh-ai-znews/znews-editorial-tools](https://github.com/latanh-ai-znews/znews-editorial-tools)**

---

## 📚 Hệ thống tài liệu kỹ thuật

Dự án được tài liệu hóa đầy đủ để các phóng viên, biên tập viên và kỹ thuật viên có thể tra cứu bất kỳ lúc nào:

| Tài liệu | Mô tả chi tiết | Đối tượng tra cứu |
|:---|:---|:---:|
| 📖 **[Sổ tay hướng dẫn sử dụng (TOOL_MANUAL.md)](./docs/TOOL_MANUAL.md)** | Hướng dẫn chi tiết từng bước cho toàn bộ 6 công cụ, thông số chuẩn, cách nhập liệu và dán mã CMS. | Phóng viên, biên tập viên, thiết kế |
| 🛡️ **[Quy chuẩn kỹ thuật CMS Ad-Safe (CMS_GUIDELINES.md)](./docs/CMS_GUIDELINES.md)** | Phân tích lỗi `layout-no-sidebar`, công thức tràn viền an toàn (`--img-bleed`), bảo vệ 3 vùng quảng cáo và font hệ thống. | Kỹ thuật viên, lập trình viên |
| 🏗️ **[Kiến trúc hệ thống (ARCHITECTURE.md)](./docs/ARCHITECTURE.md)** | Mô hình client-side, chiến lược cách ly CSS namespace, sơ đồ dữ liệu và hệ thống design system. | Lập trình viên |
| 🛠️ **[Cẩm nang nhà phát triển (DEVELOPER_GUIDE.md)](./docs/DEVELOPER_GUIDE.md)** | Hướng dẫn thiết lập máy cục bộ, quy trình thêm công cụ mới, tiêu chuẩn code và tự động hóa deploy. | Lập trình viên, DevOps |
| 🚨 **[Xử lý sự cố và khắc phục lỗi (TROUBLESHOOTING.md)](./docs/TROUBLESHOOTING.md)** | Tổng hợp các lỗi thường gặp: mất quảng cáo, vỡ thanh cuộn mobile, bẫy màu nền, co hẹp ảnh, lỗi dấu gạch ngang. | Toàn bộ đội ngũ |
| 📋 **[Nhật ký phiên bản (CHANGELOG.md)](./CHANGELOG.md)** | Lịch sử cập nhật và các cải tiến qua từng phiên bản. | Quản trị dự án |

---

## 🎛️ Danh mục các công cụ tích hợp

```
┌────────────────────────────────────────────────────────────────────────┐
│                        Studio biên tập Znews                           │
├──────────────────┬──────────────────┬──────────────────┬───────────────┤
│    Dàn trang     │    Đồ họa ảnh    │  Chuyên đề sách  │  Quy chuẩn CMS│
├──────────────────┼──────────────────┼──────────────────┼───────────────┤
│ • Magazine v10.13│ • Thumb 900×600  │ • Bài viết sách  │ • Ad-Safe Spec│
│ • No-Sidebar Ad  │ • Carousel Tool  │   (CMS Books)    │ • Bleed Rules │
│ • Photo Essay    │                  │                  │ • Color Trap  │
└──────────────────┴──────────────────┴──────────────────┴───────────────┘
```

### 1. 📰 Trình tạo layout Znews Magazine (bản 10.13)
*Tệp tin: [`tool-znews-magazine-v10-13.html`](https://latanh-ai-znews.github.io/znews-editorial-tools/tool-znews-magazine-v10-13.html)*
- Dàn trang bài viết phong cách tạp chí cao cấp (megastory, longform) với hơn 6 phong cách trình bày.
- Hiệu ứng cuộn parallax mượt mà, sticky banner và typography chuyên nghiệp.
- Cho phép nạp trực tiếp mã nguồn bài viết thô (HTML) hoặc soạn thảo từ đầu.

### 2. 🛡️ Dựng bài no side-bar (an toàn quảng cáo)
*Tệp tin: [`no-side-bar-ad-safe-tool.html`](https://latanh-ai-znews.github.io/znews-editorial-tools/no-side-bar-ad-safe-tool.html)*
- Giải pháp dàn trang đặc biệt trên layout `layout-no-sidebar` **bảo toàn 100% hiển thị cho các vùng quảng cáo** (banner đầu bài, giữa bài và chân trang).
- Tự động quét bắt trích dẫn và nhận diện chuỗi từ 3 ảnh liên tiếp trở lên để ghép thành slide hoặc lưới ảnh.

### 3. 📷 Công cụ dựng bài ảnh (photo essay)
*Tệp tin: [`photo-essay-tool.html`](https://latanh-ai-znews.github.io/znews-editorial-tools/photo-essay-tool.html)*
- Thiết kế riêng cho thể loại phóng sự ảnh, kể chuyện trực quan qua hình ảnh.
- Hỗ trợ ảnh bìa toàn cảnh, cụm ảnh đôi hoặc ba, ngắt chương hồi và chú thích ảnh chuẩn báo chí.
- Bộ chuyển đổi nhanh một chạm từ cấu trúc bài ảnh cũ sang chuẩn hiện đại.

### 4. 🖼️ Đóng khung ảnh đại diện định dạng đặc biệt (900×600)
*Tệp tin: [`Znews_Thumb_dinh_dang_dac_biet.html`](https://latanh-ai-znews.github.io/znews-editorial-tools/Znews_Thumb_dinh_dang_dac_biet.html)*
- Đóng logo định dạng chính thức của Znews (*Photo Essay, Magazine, Minimag, Longform, Special...*).
- Kéo thả, cắt cúp, phóng to thu nhỏ và điều chỉnh vị trí logo trực quan trên canvas.
- Xuất file JPG chất lượng cao đúng chuẩn kích thước **900 × 600 px** để đăng CMS.

### 5. 📚 Trình tạo bài viết sách (CMS)
*Tệp tin: [`bai-viet-sach.html`](https://latanh-ai-znews.github.io/znews-editorial-tools/bai-viet-sach.html)*
- Soạn bài điểm sách, giới thiệu tác phẩm hoặc trích đoạn sách.
- Khối thông tin sách chuyên nghiệp: bìa đứng hoặc ngang, tên tác giả, nhà xuất bản, năm phát hành, tóm tắt nổi bật.
- Tự động chuẩn hóa dấu gạch ngang dài thành dấu phẩy theo quy chuẩn biên tập Znews.
- Tách biệt CSS với namespace độc lập `.container_AI`.

### 6. 🎞️ Công cụ tạo carousel ảnh
*Tệp tin: [`carousel-tool.html`](https://latanh-ai-znews.github.io/znews-editorial-tools/carousel-tool.html)*
- Tạo slide trình chiếu ảnh nhúng gọn trong bài viết.
- Tự do định tỷ lệ hiển thị: 16:9, 4:3, 3:2, 1:1 hoặc co giãn tự động.
- Hỗ trợ chú thích từng ảnh, số trang (1/N) và tương thích cảm ứng vuốt trên thiết bị di động.

### 7. 📖 Cẩm nang quy chuẩn kỹ thuật CMS (bản số hóa)
*Tệp tin: [`guide.html`](https://latanh-ai-znews.github.io/znews-editorial-tools/guide.html)*
- Tổng hợp toàn bộ kinh nghiệm và quy tắc xử lý bố cục trang Znews dưới dạng web tương tác.
- Mục lục điều hướng thông minh, tính năng sao chép nhanh các khối code mẫu.

---

## 💻 Hướng dẫn vận hành cục bộ (offline)

Nếu bạn không có mạng Internet hoặc muốn chỉnh sửa trên máy tính:

1. **Sao chép kho lưu trữ về máy:**
   ```bash
   git clone https://github.com/latanh-ai-znews/znews-editorial-tools.git
   cd znews-editorial-tools
   ```
2. **Khởi động máy chủ tĩnh cục bộ:**
   ```bash
   # Sử dụng Python có sẵn trên máy
   python3 -m http.server 8080
   ```
3. **Mở trình duyệt:** Truy cập `http://localhost:8080`.

---

## 👥 Đóng góp và quản trị
- **Đơn vị phát triển:** Ban biên tập và đội ngũ kỹ thuật Znews.
- **Tiêu chuẩn đóng góp:** Vui lòng đọc kỹ [CONTRIBUTING.md](./CONTRIBUTING.md) trước khi gửi yêu cầu nhập mã nguồn.
- **Giấy phép:** [MIT License](./LICENSE).
