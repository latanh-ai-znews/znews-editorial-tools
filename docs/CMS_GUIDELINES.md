# Quy chuẩn kỹ thuật và bố cục CMS Znews (chuẩn an toàn quảng cáo)

Tài liệu này tổng hợp toàn bộ các quy tắc kỹ thuật, công thức tính toán CSS và các cạm bẫy thực tế khi dựng các bài viết định dạng đặc biệt (*Minimag, Longform, Special, Photo Story, no-sidebar*) trên hệ thống CMS của Znews.

---

## 📌 1. Bối cảnh: Bản chất layout CMS Znews

Khi xuất bản một bài viết được gắn cờ định dạng đặc biệt, CMS Znews sẽ áp dụng layout mang class:
```html
<div class="layout-no-sidebar"> ... </div>
```

### Hiện tượng lỗi gốc của CMS:
- Trên lý thuyết: "No side-bar" nghĩa là ẩn cột quảng cáo bên phải để bài viết mở rộng toàn trang.
- **Thực tế đã đo đạc trên hệ thống Znews**: Sidebar quảng cáo chỉ bị ẩn bằng CSS (`display: none` hoặc `visibility: hidden`), nhưng **khoảng trống ~300px của nó vẫn tồn tại** do container cha vẫn giữ định dạng Grid/Flex chia cột 2 phần:
  - Cột nội dung chính: Cố định rộng **600px**.
  - Khoảng trống sidebar ẩn: **300px + 20px gap**.
  - Tổng khung thật: **~920px - 1164px** tuỳ độ phân giải màn hình.

> [!CAUTION]
> **Hậu quả nếu ép khung toàn trang:**  
> Nếu bạn cố tình viết CSS đè lên container cha để ép cả trang rộng ra 100vw hoặc 1200px:
> 1. Toàn bộ các vùng đặt quảng cáo (banner đầu bài, banner chèn giữa các đoạn văn, banner chân trang) sẽ bị **vỡ layout, lệch khỏi khung nhìn hoặc bị che lấp hoàn toàn**.
> 2. Hệ thống tracking quảng cáo của tòa soạn sẽ ghi nhận lỗi hiển thị, gây thiệt hại doanh thu quảng cáo.

---

## 🛡️ 2. Ba vùng quảng cáo bất khả xâm phạm

Mọi bài viết dựng trên CMS Znews bắt buộc phải bảo toàn 3 vị trí quảng cáo tự động sau:
1. **Banner đầu bài (Top Leaderboard / Header Ad)**: Nằm ngay dưới tiêu đề/sapo hoặc trên khối ảnh đại diện.
2. **Khối quảng cáo giữa bài (In-Article Rectangle / Mid Banner)**: CMS tự động chèn sau đoạn văn thứ 3 hoặc thứ 5.
3. **Banner cuối bài (Bottom Ad / Footer Banner)**: Nằm ngay trước khối bài viết liên quan và bình luận.

---

## 📐 3. Kỹ thuật tràn viền cục bộ an toàn (safe local bleed)

Thay vì kéo giãn toàn bộ trang, quy tắc chuẩn là: **Chỉ cho phép từng phần tử hình ảnh hoặc trích dẫn tự tràn viền cục bộ**, trong khi khung chữ và khung quảng cáo vẫn nằm yên trong cột an toàn 600px.

### Công thức CSS chuẩn:
```css
/* Khối chứa bài viết định danh */
.znews-special-article {
  --content-width: 600px;
  --max-bleed-width: 1080px;
  /* Độ mở rộng mỗi bên */
  --img-bleed: clamp(0px, calc((100vw - var(--content-width)) / 2), 240px);
}

/* Áp dụng cho ảnh muốn mở rộng đẹp */
.znews-special-article .bleed-image {
  width: calc(100% + (var(--img-bleed) * 2));
  max-width: var(--max-bleed-width);
  margin-left: calc(var(--img-bleed) * -1);
  margin-right: calc(var(--img-bleed) * -1);
  display: block;
}

/* Áp dụng cho màn hình điện thoại (< 640px) */
@media (max-width: 640px) {
  .znews-special-article .bleed-image {
    width: 100vw;
    max-width: 100vw;
    margin-left: -16px; /* Bù trừ padding 16px mặc định của mobile */
    margin-right: -16px;
    border-radius: 0;
  }
}
```

> [!WARNING]
> **Cạm bẫy công thức cũ:**  
> Không bao giờ dùng công thức: `width: calc(100% - 40px); max-width: 866px` vì công thức này giả định phần tử cha rộng ~1164px. Khi CMS sửa lỗi hoặc trên layout mới, ảnh sẽ bị **thu nhỏ bất thường** (hẹp hơn cả cột chữ). Luôn dùng công thức tính theo `margin-left/right âm` như trên.

---

## 🎨 4. Cạm bẫy đổi bảng màu (sáng ⇄ tối)

### 4.1. Khuyến nghị mặc định: nền trắng, chữ đen
Nếu tòa soạn hoặc người biên tập không có yêu cầu đặc thù về nhận diện thương hiệu, **hãy luôn dùng nền trắng và chữ đen mặc định**.
- Lý do: Trang Znews có nền trắng. Một bài viết dùng nền xám/kem/be nhạt (như `#f3f0e9`) khi hiển thị trên màn hình sẽ tạo cảm giác một "khối màu lạ" bị lạc quẻ, thậm chí bị độc giả hiểu lầm là màn hình bị ngả vàng hoặc lỗi hiển thị.
- Để tạo điểm nhấn, chỉ cần dùng các thẻ (card), box thông tin hoặc khung trích dẫn có viền mảnh hoặc nền xám rất nhạt (`#f8fafc`).

### 4.2. Xử lý khi bắt buộc phải dùng nền tối (Dark Theme)
Nếu bài viết là phóng sự điều tra ban đêm, không gian vũ trụ... bắt buộc dùng nền tối, hãy cẩn thận với **cơ chế khoá màu 2 lớp**:
1. CMS Znews có những bộ rule CSS ghi đè bằng `!important` lên thẻ `p`, `span`, `div`.
2. Do đó, khi khai báo màu chữ cho bài tối, phải khai báo đủ cả 2 cấp:
```css
/* Cấp 1: Biến CSS tổng */
.container_dark_theme {
  --text-primary: #f8fafc;
  --bg-primary: #0b0f19;
  background-color: var(--bg-primary);
}

/* Cấp 2: Đảm bảo chống ghi đè CMS */
.container_dark_theme p,
.container_dark_theme span,
.container_dark_theme h2,
.container_dark_theme h3 {
  color: var(--text-primary) !important;
}
```

---

## 🔤 5. Quy chuẩn typography và tuyệt đối không gọi font ngoài

### 5.1. Tại sao không được gọi font ngoài?
- Nhiều bạn có thói quen nhúng `@import url('https://fonts.googleapis.com/...')` vào đầu bài.
- **Rủi ro lớn**: CMS Znews có hệ thống bảo mật Content Security Policy (CSP) chặn các domain ngoài, hoặc khi độc giả dùng mạng yếu, font ngoài tải chậm sẽ gây hiện tượng giật chữ (FOIT/FOUT). Thậm chí trên ứng dụng Znews App (WebView), việc gọi font ngoài có thể bị chặn trắng bài.

### 5.2. Font stack an toàn được khuyên dùng
Sử dụng các font chữ đã có sẵn trong hệ thống Znews hoặc font mặc định cao cấp của hệ điều hành:
```css
/* Nhóm font Serif (Dành cho Tiêu đề, Trích dẫn, Phong cách Tạp chí) */
font-family: -apple-system-ui-serif, 'Newsreader', 'Source Serif 4', 'Merriweather', 'Times New Roman', Georgia, serif;

/* Nhóm font Sans-Serif (Dành cho Thân bài, Sapo, Chú thích) */
font-family: -apple-system, BlinkMacSystemFont, 'Be Vietnam Pro', 'Inter', 'Segoe UI', Roboto, Helvetica, Arial, sans-serif;

/* Nhóm font Monospace (Dành cho Số liệu, Tag, Kicker) */
font-family: 'JetBrains Mono', SFMono-Regular, Menlo, Monaco, Consolas, monospace;
```

---

## 🧩 6. Quy chuẩn cấu trúc HTML cho phép

CMS Znews sử dụng bộ lọc mã nguồn (HTML Sanitizer) khi lưu bài. Các thẻ sau đây được hỗ trợ tốt:

| Thẻ HTML | Trạng thái | Ghi chú sử dụng |
|:---|:---:|:---|
| `<div>`, `<section>`, `<article>` | ✅ Hợp lệ | Luôn gắn class hoặc inline style có tiền tố riêng |
| `<figure>`, `<picture>`, `<img>`, `<figcaption>` | ✅ Hợp lệ | Cấu trúc chuẩn cho hình ảnh và chú thích |
| `<h1>`, `<h2>`, `<h3>`, `<p>`, `<blockquote>` | ✅ Hợp lệ | Nội dung văn bản chính |
| `<span>`, `<strong>`, `<em>`, `<b>`, `<i>` | ✅ Hợp lệ | Định dạng cục bộ |
| `<button>`, `<a>` | ✅ Hợp lệ | Nút tương tác và liên kết nội bộ |
| `<svg>`, `<path>` | ⚠️ Hạn chế | Hợp lệ nhưng nên để kích thước cố định `width`/`height` |
| `<style>` | ✅ Chấp nhận | Phải đặt trong khối cha và scoped rõ ràng |
| `<script>` | ⚠️ Hạn chế | CMS có thể cắt script nếu chứa hàm can thiệp DOM ngoài container |
| `<iframe>` | ❌ Bị lọc | Thường bị CMS chặn trừ khi là iframe nhúng đã whitelist (YouTube) |

---

## ✅ 7. Pre-flight Checklist (Kiểm tra trước khi bấm Đăng)

Trước khi gửi duyệt hoặc xuất bản bài viết trên CMS, hãy tích chọn đủ 7 bước kiểm tra sau:

- [ ] **1. Kiểm tra Quảng cáo**: Banner trên cùng, banner giữa bài và banner chân trang có hiển thị trơn tru không? Có bị ảnh hoặc khối nào che lấp không?
- [ ] **2. Kiểm tra Mobile**: Mở bằng điện thoại hoặc bật F12 Mobile View, vuốt dọc từ trên xuống dưới có bị thanh cuộn ngang (horizontal scroll) không?
- [ ] **3. Kiểm tra Dấu câu**: Tất cả các gạch ngang dài (`—`, `–`) đã được chuyển thành dấu phẩy đúng chuẩn Znews chưa?
- [ ] **4. Kiểm tra Chú thích ảnh**: Mọi ảnh minh họa đều đã có nguồn ảnh (Photo: ...) và chú thích rõ ràng chưa?
- [ ] **5. Kiểm tra Nền bài viết**: Nếu dùng nền trắng, các box có độ tương phản đủ nét chưa? Nếu dùng nền tối, chữ có bị CMS biến thành đen xì không?
- [ ] **6. Kiểm tra Font chữ**: Font có hiển thị mượt mà không? Có bị lỗi ô vuông hoặc gõ tiếng Việt bị lỗi dấu không?
- [ ] **7. Kiểm tra Namespace CSS**: Mọi CSS viết ra có nằm gọn trong class bao bọc (Ví dụ: `.znews-magazine-wrap`, `.container_AI`) để không ảnh hưởng đến header/footer chung của báo không?
