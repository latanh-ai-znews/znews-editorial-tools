# Hướng dẫn dựng "bài đặc biệt dạng no side-bar, có hiển thị quảng cáo" cho CMS Znews

Tài liệu này tổng hợp toàn bộ quy tắc, mẫu code và lỗi đã gặp khi dựng các bài
"đặc biệt" (minimag, longform, có hero/carousel/pull-quote riêng) để dán vào
CMS Znews. Dùng tài liệu này làm ngữ cảnh khi nhờ bất kỳ AI nào (Claude, GPT,
Gemini...) dựng hoặc chỉnh sửa loại bài này, để tránh lặp lại các lỗi đã từng
gặp.

**Tên gọi chuẩn cho định dạng này: "bài đặc biệt dạng no side-bar, có hiển
thị quảng cáo"** — gọi vậy vì CMS render các bài này trên layout mang class
`layout-no-sidebar` (sidebar quảng cáo bị ẩn nhưng khoảng trống của nó vẫn
tồn tại do lỗi CSS gốc, xem mục 2), và mục tiêu bắt buộc của định dạng là
các vùng quảng cáo trong bài (ảnh đầu bài, khối giữa bài, banner cuối bài)
vẫn hiển thị được bình thường — khác với các mẫu tràn viền cũ (mục 5) vốn
che mất quảng cáo.

---

## 1. Bối cảnh: vì sao cần tài liệu này

Các bài "đặc biệt" là một khối `<style>` + `<article>` + `<script>` tự chứa,
dán trực tiếp vào khung soạn thảo CMS. Khối này chạy trong CÙNG một trang với
toàn bộ giao diện thật của Znews — bao gồm quảng cáo, sidebar, header, footer.
Rất nhiều lỗi từng gặp không phải do sai nội dung, mà do CSS/JS của bài vô
tình:

- Đè lên vùng quảng cáo thật.
- Ép trang thật đổi kích thước/hành vi.
- Gọi tài nguyên ngoài (font) không cần thiết.
- Bị chính khung soạn thảo (contenteditable) của CMS hiểu sai vị trí.

---

## 2. Ràng buộc kỹ thuật đã đo được từ trang thật

Đo bằng DevTools/agent duyệt web trên `tech.zingnews.vn` (viewport desktop
~1268px):

- `SECTION.main` (khung chứa toàn bài): rộng **1164px**.
- `.the-article-body` (cột nội dung bài): **`width:600px`**, nhưng có
  `margin:0 0 0 -300px` — đây là lỗi CSS gốc của trang (bù trừ cho một
  sidebar quảng cáo `#sidebarArticle` rộng 300px đang bị `display:none` chứ
  không bị gỡ khỏi layout). Hệ quả: cột nội dung lệch trái, để lại khoảng
  trống ~264px bên phải — **đó chính là vùng dự phòng cho quảng cáo**, dù
  quảng cáo có hiện hay không.
- Có 2 vùng quảng cáo dạng tĩnh (nằm trong luồng, không phải overlay):
  `#ZingNews_Article_Image` (trong khung ảnh đầu bài) và
  `#ZingNews_Masthead_Inline_1` (chèn giữa nội dung bài, bên trong
  `<article>`).
- Có 1 banner **dính khi cuộn** (`position:sticky; top:70px`), kích thước
  300×600, xuất hiện ở khu vực "đọc thêm" cuối bài (`#article-nextreads`).
- Phần tử `position:fixed` duy nhất trên trang là thanh header (cao 52px).
- Ảnh do CMS tự chèn qua cấu trúc bảng cũ (`<table style="margin-left:-130px;
  width:860px">...`) đạt chiều rộng thực tế **860px** — tức bung ra khỏi cột
  600px thêm đúng **130px mỗi bên**. Đây là con số tham chiếu an toàn cho
  ảnh cần "to hơn cột chữ" trong các bài đặc biệt.

### Quy tắc suy ra từ số đo trên

1. **Không bao giờ** ép `.the-article-body` hay `.main` đổi `width`,
   `max-width`, `margin`, `padding`, `overflow` bằng CSS trong bài. Đây là
   khung của TRANG THẬT, không phải của bài — sửa nó là sửa layout toàn
   trang, phá luôn không gian dành cho quảng cáo (từng gặp lỗi này y hệt: một
   bài ép `.the-article-body{width:100%!important;overflow:visible!important}`
   khiến quảng cáo biến mất hoàn toàn).
2. **Không dùng kỹ thuật tràn viền toàn màn hình**
   (`width:100vw; margin-left:calc(50% - 50vw)`) cho bất kỳ phần tử nào —
   kể cả chỉ ở phần hero. 100vw luôn rộng hơn 600px rất nhiều, chắc chắn đè
   lên vùng quảng cáo dù quảng cáo có hiện hay không.
3. Nếu cần ảnh/khối to hơn cột chữ (giống cách CMS tự làm), dùng **"tràn cục
   bộ" có kiểm soát**, không phải tràn toàn viewport:
   ```css
   .khoi-anh{
     margin-left: -130px;
     margin-right: -130px;
     width: calc(100% + 260px);
   }
   /* Bắt buộc: reset về 0 khi màn hình hẹp, vì cột 600px chỉ tồn tại ở
      desktop — dưới mobile toàn bộ layout co giãn khác hẳn */
   @media (max-width: 700px){
     .khoi-anh{ margin-left:0; margin-right:0; width:100%; }
   }
   ```
   130px mỗi bên là con số đã kiểm chứng khớp với cách CMS tự hiển thị ảnh
   full-width thật — dùng làm mặc định, có thể chỉnh nếu đo lại ra số khác.
4. Nếu bài cần hiệu ứng "hero tràn màn hình" kiểu tạp chí (ảnh lớn, chữ đè
   lên ảnh, chiếm gần hết viewport) — **không làm được an toàn** trong ràng
   buộc 600px này. Phải hạ cấp xuống bố cục xếp chồng bình thường (tiêu đề/
   sapo phía trên, ảnh hero bên dưới, dùng đúng kỹ thuật tràn cục bộ ở mục 3).
5. **Khi sửa một bài cũ để bỏ đoạn CSS ép khung trang thật (mục 1)**, phải
   rà lại TOÀN BỘ công thức chiều rộng nào tính theo `%`/`calc()` của
   phần tử cha — nhiều bài cũ viết công thức kiểu
   `width:calc(100% - 40px); max-width:866px` với giả định phần tử cha
   rộng ~1164px (do từng bị ép khung). Bỏ đoạn ép khung mà không sửa lại
   công thức này sẽ khiến ảnh **hẹp lại bất ngờ** (có khi hẹp hơn cả cột
   chữ) thay vì tràn ra — nhìn qua tưởng là "chưa tràn được" nhưng thực ra
   do công thức cũ tính sai trên nền khung mới. Luôn đổi các công thức kiểu
   này sang đúng công thức "tràn cục bộ" ở mục 3
   (`margin-left/right: calc(var(--img-bleed) * -1)`), không giữ lại công
   thức `calc(100% - Npx)` kiểu cũ.

---

## 3. Không gọi font ngoài

Nếu người biên tập yêu cầu "dùng font mặc định CMS" / "không gọi font
ngoài":

- Xoá mọi `@import url('https://fonts.googleapis.com/...')`.
- Đổi mọi biến font (`--zac-disp`, `--zac-sans`, `--zac-body`...) thành
  `inherit` thay vì tên font cụ thể (`"Newsreader"`, `"Manrope"`...).
- **Cạm bẫy**: `inherit` **không hợp lệ** khi nằm trong cú pháp rút gọn
  `font: <weight> <size>/<line-height> <family>;`. Nếu dùng
  `font: 600 15px/1 var(--ten-bien)` mà biến đó là `inherit`, cả khai báo có
  thể bị trình duyệt coi là không hợp lệ và bỏ qua toàn bộ (mất luôn cả
  size/weight, không chỉ mất font). Bắt buộc phải tách riêng từng thuộc
  tính khi dùng `inherit`:
  ```css
  /* SAI — có thể làm hỏng cả rule */
  .nhan{ font: 600 15px/1 var(--font-bien-la-inherit); }

  /* ĐÚNG */
  .nhan{ font-weight:600; font-size:15px; line-height:1; font-family:inherit; }
  ```
- Ở phần tử gốc của bài, khai báo thêm `font-family:inherit!important;` để
  chống trường hợp CSS mặc định của CMS có rule tổng quát ghi đè ngược lại.

---

## 4. Cấu trúc HTML được CMS chấp nhận

CMS lọc/loại bỏ một số thẻ và thuộc tính khi lưu bài. Luôn tuân thủ:

- **Không dùng `<span>`, không dùng `<button>` thật.** Với phần tử cần bấm
  được (nút carousel, tab...), dùng `<div role="button" tabindex="0">` hoặc
  `<div role="tab">` thay thế.
- **Không dùng thuộc tính `style="..."` nội tuyến.** Mọi định vị/màu sắc
  phải nằm trong khối `<style>` dùng class.
- Comment trong `<script>` chỉ dùng `/* ... */`, **không dùng `//`** — CMS
  gộp nội dung `<script>` thành một dòng duy nhất khi lưu, dấu `//` sẽ nuốt
  mất toàn bộ phần code phía sau nó trên "dòng" đó.
- Ảnh chèn qua CMS thường có cấu trúc `<table class="picture">` — cần có
  rule khử wrapper này về `display:block;width:100%` để ảnh vào đúng layout
  của bài, tránh giữ nguyên bảng/canh giữa mặc định của CMS.
- Giữ nguyên `imgid` trên thẻ `<img>` nếu CMS đã gán — đây là cách CMS nhận
  diện ảnh đã upload, đổi hoặc xoá thuộc tính này có thể khiến ảnh không
  hiển thị.

---

## 5. Chỉ dùng khi bài BẮT BUỘC phải tràn viền: cơ chế "ngủ / đánh thức"

Nếu bài cũ hơn đã lỡ dùng tràn viền (`width:100vw`) và không tiện dựng lại
từ đầu, khung soạn thảo CMS (vùng `contenteditable`) sẽ tính sai vị trí vì
layout của nó không đối xứng như trang thật — dẫn đến nội dung bị lệch, cắt
mất chữ khi đang sửa bài (dù trang thật vẫn hiển thị đúng). Cách xử lý: cho
class gốc "ngủ" trong lúc soạn thảo, "đánh thức" lại khi ra trang thật.

**"Bài đặc biệt dạng no side-bar, có hiển thị quảng cáo" (dựng theo mục 2-4
ở trên, không tràn viền) thì KHÔNG cần cơ chế này** — mục này chỉ áp dụng
cho các mẫu tràn viền kiểu cũ, đây là lưới an toàn dự phòng cho loại bài
khác, không phải bước bắt buộc cho định dạng chính của tài liệu này.

Bốn chỗ cần chèn, đúng thứ tự:

```html
<!-- 1. Ngay trước <style> -->
<script>
window.ZAC_EDIT = false;
window.zacWake = function(id, cls){
  var w = document.getElementById(id);
  if (!w) return;
  if ((w.closest && w.closest('[contenteditable="true"]')) || document.designMode === 'on') {
    window.ZAC_EDIT = true;
    return;
  }
  w.className = cls;
};
</script>

<!-- 2. Khối gốc: class ngủ + dòng đánh thức ngay sau thẻ mở -->
<article class="ten-class-sleep" id="idBaiViet"><script>window.zacWake('idBaiViet','ten-class-goc');</script>

<!-- 3. Đầu mọi IIFE hiệu ứng trong <script> -->
(function(){ if (window.ZAC_EDIT) { return; }

<!-- 4. Cuối <style>: CSS riêng cho chế độ soạn thảo -->
```

CSS chế độ soạn thảo (mẫu, chỉ bám class-sleep nên biến mất hoàn toàn khi
đánh thức):

```css
.ten-class-sleep{max-width:760px;margin:24px auto;padding:0 16px;background:#fff;color:#111;font-size:16px;line-height:1.65}
.ten-class-sleep svg,.ten-class-sleep [aria-hidden="true"]{display:none!important}
.ten-class-sleep img{width:auto!important;height:auto!important;max-width:300px!important}
/* + rule riêng cho từng khối trang trí đặc thù của bài, ví dụ: hiện lại hết
   caption carousel đang bị "hidden" để phóng viên thấy đủ mà sửa */
.ten-class-sleep .carousel-cap p[hidden]{display:block!important}
.ten-class-sleep .carousel-nav{display:none!important}
```

Kiểm tra trước khi giao bài:
- Mở file bằng trình duyệt thường: phải thấy giao diện đầy đủ ngay, không
  nháy lúc load.
- Chuỗi tên class-sleep chỉ được xuất hiện ở thuộc tính `class` của khối gốc
  và trong khối CSS chế độ soạn thảo — không lọt ra chỗ khác.
- Không còn `//` trong bất kỳ khối `<script>` nào.

---

## 6. Thành phần tái dùng được

### 6.1. Pull-quote (trích dẫn nổi bật)

Quy tắc bắt buộc: **câu quote khi tách thành khối trích dẫn riêng vẫn phải
giữ nguyên trong đoạn văn thân bài** (kèm "X nói/chia sẻ/nhận định"). Pull-
quote là NHẮC LẠI để nhấn mạnh, không phải RÚT câu đó khỏi mạch văn — từng
làm sai điều này (xoá quote khỏi thân bài khi tách riêng) khiến mạch văn bị
cụt.

Nếu bài có nhiều câu đáng trích hơn số lượng cần dùng và không có tiêu chí
rõ ràng để chọn, hỏi người biên tập chọn câu nào — đừng tự đoán, nhất là khi
tiêu đề bài đã gợi ý sẵn 2-3 hướng cần minh hoạ riêng.

Có thể cho quote hiển thị **trái/phải** (float, chữ bọc quanh) hoặc **giữa**
(khối riêng, đầy đủ chiều rộng cột) — không có kỹ thuật nào trong hai kiểu
này vi phạm ràng buộc mục 2, miễn quote không rộng hơn cột 600px.

### 6.2. Carousel ảnh (gộp từ 3+ ảnh liên tiếp)

Khi nội dung gốc có từ 3 ảnh liên tiếp trở lên cùng chủ đề, nên gộp thành
carousel thay vì để rời từng ảnh.

**Lỗi từng gặp và phải tránh lặp lại**: KHÔNG được đặt việc khởi tạo
carousel phụ thuộc vào cùng điều kiện với hiệu ứng "hiện dần khi cuộn"
(`IntersectionObserver` / `prefers-reduced-motion`). Nếu gộp chung một nhánh
`if`, máy nào tắt hiệu ứng chuyển động hoặc trình duyệt không hỗ trợ
`IntersectionObserver` sẽ khiến carousel **mất luôn khả năng bấm/vuốt** —
carousel là chức năng chính, phải luôn luôn khởi tạo, không được xem là
hiệu ứng trang trí có thể bỏ qua.

```js
/* Hiệu ứng cuộn — CÓ THỂ bỏ qua nếu trình duyệt không hỗ trợ */
if (!reduce && ("IntersectionObserver" in window)) {
  /* ...gắn observer cho hiệu ứng hiện dần... */
}
/* Carousel — LUÔN khởi tạo, không đặt trong nhánh if ở trên */
document.querySelectorAll(".carousel").forEach(function(car){ /* ...gắn sự kiện bấm/vuốt... */ });
```

Ảnh trong carousel nên cắt theo một `aspect-ratio` cố định (vd `3/2` +
`object-fit:cover`) để mọi slide cao bằng nhau dù ảnh gốc lệch tỷ lệ.

### 6.3. Tiêu đề chương / chip màu

- Nếu dùng ô màu (chip) làm nền cho tiêu đề chương: màu nền có thể rực rỡ
  thoải mái vì chữ đè lên luôn cố định màu tối — không phụ thuộc nền trang
  sáng hay tối.
- Nếu CÙNG một màu đó lại dùng làm MÀU CHỮ (ví dụ nhãn nhỏ, link) trên nền
  trang sáng, phải dùng bản đậm hơn hẳn — màu pastel/neon vốn được chọn để
  làm nền, không phải để làm chữ, dùng thẳng sẽ khó đọc hoặc gần như vô
  hình. Nên tách hẳn hai biến CSS cho hai vai trò này (`--mau-nen-chip` và
  `--mau-chu-nhan`) thay vì dùng chung một biến.
- Không đánh số tự động kiểu "{ 01 }", "{ 02 }" trước mỗi tiêu đề chương nếu
  không được yêu cầu — nhiều biên tập viên không muốn kiểu đánh số này,
  chỉ cần tiêu đề chương là đủ.

---

## 7. Cạm bẫy đổi bảng màu (sáng ⇄ tối)

**Khuyến nghị mặc định**: nếu người biên tập không yêu cầu cụ thể một tông
màu nền riêng, nên bỏ hẳn màu nền tuỳ chỉnh cho toàn bài (kể cả các tông
tưởng chừng trung tính như kem/be/pastel) và dùng **nền trắng, chữ đen** —
đúng màu nền thật của trang Znews. Lý do:

- Bài hoà thẳng vào trang, không tạo cảm giác "khối lạ" chèn giữa nội dung
  trắng của toàn site.
- Nhiều tông kem/be nhạt (ví dụ `#f3f0e9`) khi lên màn hình dễ bị nhìn
  thành "ngả vàng" dù ý đồ ban đầu chỉ là tạo chất giấy — từng phải sửa lại
  một bài đúng vì lý do này.
- Đỡ phải lo việc khoá màu 2 lớp ở trên khi không thực sự cần một bảng màu
  riêng.

Chỉ cần các "thẻ" (box sách, khung ảnh chờ tải, box trích dẫn) tự tạo tương
phản bằng viền/bóng đổ nhẹ hoặc một lớp xám rất nhạt (`#f2f2f2` trở lên),
không cần cả trang phải nhuốm màu.

Nếu người dùng CÓ yêu cầu một bảng màu riêng (nền tối, nền màu thương
hiệu...), mới áp dụng theo yêu cầu — và khi đó, các cạm bẫy dưới đây bắt
đầu phát huy tác dụng:

Rất nhiều mẫu bài "khoá" màu bằng cách khai báo lại **hai lần**: một lần
bằng biến CSS ở đầu file (để các rule dùng `var()` ăn theo), một lần bằng
mã màu cứng ở cuối file với `!important` (để chống CMS ghi đè). Khi đổi
bảng màu, quên sửa MỘT trong hai chỗ là nguyên nhân phổ biến nhất khiến đổi
màu "không ăn" — phải rà cả hai.

Khi chuyển bài từ nền tối sang nền sáng (hoặc ngược lại), luôn kiểm tra lại
độ tương phản chữ/nền cho từng cặp màu đã đổi, không chỉ đảo ngược
nền/chữ chính rồi dừng — các màu phụ (link, nhãn nhỏ, viền) thường cần một
giá trị khác hẳn để vẫn đọc được, không thể chỉ đảo đen-trắng máy móc.

---

## 8. Ẩn tiêu đề/sapo mặc định của CMS (chỉ khi bài tự vẽ hero riêng)

Nếu bài tự dựng tiêu đề/sapo/tác giả riêng (dạng minimag), cần ẩn phần CMS
tự sinh để tránh hiển thị trùng lặp:

```css
.the-article:has(#idBaiViet) .the-article-category,
.the-article:has(#idBaiViet) .the-article-summary,
.the-article:has(#idBaiViet) .the-article-meta { display:none!important; }
.the-article:has(#idBaiViet) .the-article-title {
  position:absolute!important; width:1px!important; height:1px!important;
  margin:-1px!important; overflow:hidden!important;
  clip:rect(0 0 0 0)!important; clip-path:inset(50%)!important; white-space:nowrap!important;
}
```

Đây là NGOẠI LỆ duy nhất được phép nhắm tới phần tử của trang thật (chỉ ẩn
hiển thị, không đổi kích thước/vị trí/overflow nên không ảnh hưởng tới
quảng cáo). Nếu bài KHÔNG tự vẽ tiêu đề riêng (dùng luôn tiêu đề/sapo CMS
sinh), bỏ qua mục này hoàn toàn.

---

## 9. Quy trình khi nhận yêu cầu dựng/sửa một bài

1. Xác định bài có cần tự vẽ tiêu đề/sapo riêng không (minimag) hay dùng
   tiêu đề CMS (bài thường). Việc này quyết định có cần mục 8 hay không.
2. Dựng nội dung theo cấu trúc chương/đoạn/ảnh, áp cả bốn ràng buộc ở mục
   2-4 ngay từ đầu — đừng dựng xong rồi mới "vá" an toàn quảng cáo sau,
   dễ sót.
3. Nếu có ≥3 ảnh liên tiếp → carousel (mục 6.2). Nếu có nhiều câu quote hay
   → hỏi người dùng chọn câu nào trước khi tách pull-quote (mục 6.1).
4. Chỉ dùng cơ chế ngủ/đánh thức (mục 5) nếu vì lý do nào đó bài vẫn cần
   tràn viền — với bài dựng mới theo tài liệu này thì không cần.
5. Tự kiểm tra trước khi giao: không còn `100vw`, không có rule nào nhắm
   `.the-article-body`/`.main` để đổi width/overflow, không gọi font ngoài,
   không còn `<span>`/`<button>`/`style="..."` trong nội dung bài, JS hợp
   lệ (không có `//` trong script), carousel (nếu có) khởi tạo độc lập với
   hiệu ứng cuộn.
