# Studio biên tập Znews — Bộ công cụ dàn trang và xuất bản báo chí

[![GitHub Pages](https://img.shields.io/badge/GitHub%20Pages-Live%20Website-success?style=for-the-badge&logo=github)](https://latanh-ai-znews.github.io/znews-editorial-tools/)
[![Version](https://img.shields.io/badge/Version-2.4.1-blue?style=for-the-badge)](CHANGELOG.md)
[![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)](LICENSE)
[![Platform](https://img.shields.io/badge/Platform-Web%20%7C%20Mobile%20%7C%20Desktop-orange?style=for-the-badge)](index.html)

Hệ thống công cụ chuyên nghiệp phục vụ công tác dàn trang magazine, phỏng vấn chuyên sâu (interview tool), bài so sánh đối chiếu (comparison tool), phóng sự ảnh (photo essay), đóng khung ảnh đại diện chuẩn 900×600, tạo slide ảnh (carousel) và soạn thảo bài viết chuyên đề chuẩn CMS báo điện tử **Znews**.

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
| 📖 **[Sổ tay hướng dẫn sử dụng (TOOL_MANUAL.md)](./docs/TOOL_MANUAL.md)** | Hướng dẫn chi tiết từng bước cho toàn bộ 8 công cụ, thông số chuẩn, cách nhập liệu và dán mã CMS. | Phóng viên, biên tập viên, thiết kế |
| 🛡️ **[Quy chuẩn kỹ thuật CMS Ad-Safe (CMS_GUIDELINES.md)](./docs/CMS_GUIDELINES.md)** | Phân tích lỗi `layout-no-sidebar`, công thức tràn viền an toàn (`--img-bleed`), bảo vệ 3 vùng quảng cáo và font hệ thống. | Kỹ thuật viên, lập trình viên |
| 🏗️ **[Kiến trúc hệ thống (ARCHITECTURE.md)](./docs/ARCHITECTURE.md)** | Mô hình client-side, chiến lược cách ly CSS namespace, sơ đồ dữ liệu và hệ thống design system. | Lập trình viên |
| 🛠️ **[Cẩm nang nhà phát triển (DEVELOPER_GUIDE.md)](./docs/DEVELOPER_GUIDE.md)** | Hướng dẫn thiết lập máy cục bộ, quy trình thêm công cụ mới, tiêu chuẩn code và tự động hóa deploy. | Lập trình viên, DevOps |
| 🚨 **[Xử lý sự cố và khắc phục lỗi (TROUBLESHOOTING.md)](./docs/TROUBLESHOOTING.md)** | Tổng hợp các lỗi thường gặp: mất quảng cáo, vỡ thanh cuộn mobile, bẫy màu nền, co hẹp ảnh, lỗi tràn viền 130px. | Toàn bộ đội ngũ |
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
│ • Photo Essay v3 │                  │                  │ • Color Trap  │
│ • Interview Tool │                  │                  │               │
│ • Comparison Tool│                  │                  │               │
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

### 3. 📷 Công cụ dựng bài ảnh (photo essay v3)
*Tệp tin: [`photo-essay-tool.html`](https://latanh-ai-znews.github.io/znews-editorial-tools/photo-essay-tool.html)*
- Thiết kế riêng cho thể loại phóng sự ảnh, kể chuyện trực quan qua hình ảnh.
- Bản 3.0: tự động tối ưu độ phân giải ảnh theo kích thước màn hình (thang ladder w360 - w1920), cơ chế chống méo tỷ lệ ảnh (ratio drift guard), tự đồng bộ breadcrumb chuyên mục từ CMS và lightbox zoom sắc nét tối đa.
- Hỗ trợ ảnh bìa toàn cảnh, cụm ảnh đôi hoặc ba, ngắt chương hồi và chú thích ảnh chuẩn báo chí.

### 4. 🎙️ Công cụ dựng bài phỏng vấn (interview tool)
*Tệp tin: [`interview-tool.html`](https://latanh-ai-znews.github.io/znews-editorial-tools/interview-tool.html)*
- Dành riêng cho thể loại bài phỏng vấn, tọa đàm chuyên sâu với chuyên gia và nhân vật đặc biệt.
- Tùy chọn 2 phong cách hỏi–đáp: 1 cột kinh điển và 2 cột cố định câu hỏi (sticky side) khi cuộn nội dung dài.
- Tự động chia phần đánh số, tạo mục lục (TOC), chèn trích dẫn, ảnh minh họa và dải số liệu thống kê.
- Khắc phục triệt để lỗi tràn viền 130px trên bố cục `layout-special` của CMS và tự động giới hạn độ rộng cột chữ (760px) cho trải nghiệm đọc tối ưu trên màn hình lớn.

### 5. ⚖️ Công cụ bài so sánh đối chiếu (comparison tool)
*Tệp tin: [`comparison-tool.html`](https://latanh-ai-znews.github.io/znews-editorial-tools/comparison-tool.html) | [Bài viết demo trực tuyến](https://latanh-ai-znews.github.io/znews-editorial-tools/demo-bai-viet-so-sanh.html)*
- Dành riêng cho thể loại bài viết so sánh đa chiều, phân tích đối lập "Đánh đổi vs Lợi ích", "Trước vs Sau", "Lựa chọn A vs B".
- **Hệ thống thẩm mỹ cao cấp**: Phong cách **Officevibe Editorial** (nền Warm Canvas `#f9f8f6`, viền Cream Border `#f0e9e1`, tít Ink Navy `#0c1754` với chữ nghiêng *italic accent* mang tính văn chương, nút bấm Electric Cobalt `#2545ff` bo pill 100px) kết hợp tùy chọn **Superr Notebook** (giấy kem, viền than 1.5px, bút dạ cam).
- Cơ chế ẩn hiện triệt để hai vế: khi xem góc nhìn Đánh đổi thì Lợi ích ẩn hoàn toàn 100% và ngược lại, giúp thao tác trượt mở thực sự có ý nghĩa.
- Khung nội dung tích hợp (Integrated Visual Frame): ảnh sắc nét và cột văn bản phân tích (1–3 đoạn) nằm liền khối, tự động cân đối tỷ lệ trên mọi kích cỡ màn hình.
- Thanh trượt kiểu iPhone chuyển cảnh mượt mà kèm dòng chữ phát sáng nhấp nháy, hỗ trợ vuốt chạm trên màn hình cảm ứng.
- Đi kèm trang bài viết demo mẫu [`demo-bai-viet-so-sanh.html`](https://latanh-ai-znews.github.io/znews-editorial-tools/demo-bai-viet-so-sanh.html) hỗ trợ 3 chế độ xem (Máy tính, Di động 420px, Mô phỏng CMS Znews).

### 6. 🖼️ Đóng khung ảnh đại diện định dạng đặc biệt (900×600)
*Tệp tin: [`Znews_Thumb_dinh_dang_dac_biet.html`](https://latanh-ai-znews.github.io/znews-editorial-tools/Znews_Thumb_dinh_dang_dac_biet.html)*
- Đóng logo định dạng chính thức của Znews (*Photo Essay, Magazine, Minimag, Longform, Special...*).
- Kéo thả, cắt cúp, phóng to thu nhỏ và điều chỉnh vị trí logo trực quan trên canvas.
- Xuất file JPG chất lượng cao đúng chuẩn kích thước **900 × 600 px** để đăng CMS.

### 7. 📚 Trình tạo bài viết sách (CMS)
*Tệp tin: [`bai-viet-sach.html`](https://latanh-ai-znews.github.io/znews-editorial-tools/bai-viet-sach.html)*
- Soạn bài điểm sách, giới thiệu tác phẩm hoặc trích đoạn sách.
- Khối thông tin sách chuyên nghiệp: bìa đứng hoặc ngang, tên tác giả, nhà xuất bản, năm phát hành, tóm tắt nổi bật.
- Tự động chuẩn hóa dấu gạch ngang dài thành dấu phẩy theo quy chuẩn biên tập Znews.
- Tách biệt CSS với namespace độc lập `.container_AI`.

### 8. 🎞️ Công cụ tạo carousel ảnh
*Tệp tin: [`carousel-tool.html`](https://latanh-ai-znews.github.io/znews-editorial-tools/carousel-tool.html)*
- Tạo slide trình chiếu ảnh nhúng gọn trong bài viết.
- Tự do định tỷ lệ hiển thị: 16:9, 4:3, 3:2, 1:1 hoặc co giãn tự động.
- Hỗ trợ chú thích từng ảnh, số trang (1/N) và tương thích cảm ứng vuốt trên thiết bị di động.

### 9. 📖 Cẩm nang quy chuẩn kỹ thuật CMS (bản số hóa)
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
