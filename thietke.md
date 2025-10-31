khoj
├── [RED] Dockerfile                  // build dev image (backend + deps)
├── [RED] computer.Dockerfile         // image cho “Khoj computer” RPA sandbox
├── [RED] prod.Dockerfile             // build image sản xuất tối ưu
├── [RED] docker-compose.yml          // orchestration Postgres/pgvector, sandbox, SearxNG, server
├── [RED] pyproject.toml              // cấu hình Python package, deps, script
├── [RED] uv.lock                     // lock deps cho Hatch/uv
├── [RED] README.md                   // mô tả dự án, hướng dẫn tổng quan
├── [RED] LICENSE                     // giấy phép AGPL
├── [RED] manifest.json               // metadata plugin (Obsidian/Desktop)
├── [RED] pytest.ini                  // cấu hình pytest mark & options
├── [RED] gunicorn-config.py          // cấu hình gunicorn (prod)
├── [RED] versions.json               // version mapping (client/server)
├── [RED] .devcontainer/              // cấu hình VS Code dev-container
├── [RED] .github/                    // workflow CI/CD, issue template
│   ├── [RED] workflows/              // pipeline test, docker, release
│   └── [WHITE] templates/insurance_bot_guidelines.md // hướng dẫn mở issue cho chatbot bảo hiểm
├── [RED] .vscode/                    // settings, launch config VS Code
├── [RED] documentation/              // tài liệu chính thức
│   ├── [RED] assets/                 // hình ảnh minh họa
│   ├── [RED] docs/                   // nội dung docs cấu trúc theo danh mục
│   │   ├── [RED] get-started/        // hướng dẫn cài đặt nhanh
│   │   ├── [RED] features/           // mô tả tính năng
│   │   ├── [RED] data-sources/       // cấu hình nhập dữ liệu
│   │   ├── [RED] clients/            // tài liệu cho client (web, mobile…)
│   │   ├── [RED] advanced/           // triển khai nâng cao, scaling
│   │   ├── [RED] contributing/       // hướng dẫn đóng góp
│   │   └── [WHITE] insurance/        // chuyên mục kiến thức bảo hiểm
│   │       ├── [WHITE] underwriting_faq.md       // FAQ thẩm định, underwriting
│   │       ├── [WHITE] claims_playbook.md        // quy trình xử lý bồi thường
│   │       └── [WHITE] compliance_checklist.md   // checklist tuân thủ bảo hiểm
│   └── [RED] src/                    // code nguồn trang docs
│       └── [WHITE] components/InsuranceUseCases.tsx // component hiển thị use-case bảo hiểm
├── [RED] migrations/                 // migration Django
├── [RED] scripts/                    // script tiện ích
│   └── [WHITE] load_insurance_corpus.py // script nạp dữ liệu bảo hiểm vào DB/pgvector
├── [RED] src/                        // mã nguồn chính
│   ├── [RED] interface/              // client ứng dụng (Web/Desktop/Obsidian…)
│   │   ├── [RED] web/                // web client Next.js
│   │   ├── [RED] desktop/            // Electron app
│   │   ├── [RED] obsidian/           // plugin Obsidian
│   │   ├── [RED] emacs/              // plugin Emacs
│   │   └── [RED] android/            // app Android
│   ├── [RED] telemetry/              // thu thập telemetry (opt-in)
│   └── [RED] khoj/                   // backend FastAPI + Django
│       ├── [RED] main.py             // entry point khởi chạy server, scheduler
│       ├── [RED] configure.py        // middleware, auth, jobs, config hệ thống
│       ├── [RED] manage.py           // CLI quản trị Django
│       ├── [RED] app/                // cấu hình Django (settings, urls)
│       ├── [RED] routers/            // REST/Websocket API endpoints
│       │   ├── [RED] api.py          // router bao quát cho API chính
│       │   ├── [RED] api_chat.py     // endpoint chat agent
│       │   ├── [RED] api_agents.py   // CRUD agent tùy biến
│       │   ├── [RED] api_content.py  // upload, quản lý nguồn dữ liệu
│       │   ├── [RED] api_automation.py // điều phối automation
│       │   ├── [RED] api_phone.py    // webhook thoại/SMS
│       │   ├── [RED] api_subscription.py // quản lý subscription, billing
│       │   ├── [RED] api_model.py    // cấu hình model, inference endpoint
│       │   ├── [RED] chat.py         // web chat interface
│       │   ├── [RED] research.py     // mode /research
│       │   ├── [RED] storage.py      // file storage API
│       │   ├── [RED] email.py        // email webhook
│       │   ├── [RED] notion.py       // đồng bộ Notion
│       │   ├── [RED] twilio.py       // tích hợp Twilio/WhatsApp
│       │   └── [WHITE] insurance.py  // API chuyên biệt kịch bản bảo hiểm (tra cứu hợp đồng, báo giá…)
│       ├── [RED] processor/          // xử lý tài liệu, RAG, tool pipeline
│       │   ├── [RED] embeddings.py   // quản lý embedding & rerank model
│       │   ├── [RED] content/        // converter cho PDF/DOCX/Markdown/…
│       │   ├── [RED] conversation/   // điều phối hội thoại, state machine
│       │   ├── [RED] image/          // OCR, xử lý ảnh
│       │   ├── [RED] speech/         // chuyển giọng nói
│       │   ├── [RED] operator/       // automation “computer”
│       │   └── [RED] tools/          // tool plugin cho agent
│       │       ├── [RED] insurance_tools.py // tool ví dụ xử lý dữ liệu bảo hiểm (đã có)
│       │       └── [WHITE] claims_workflow.py // tool tự động hoá quy trình bồi thường
│       ├── [RED] database/           // ORM, adapters, management command
│       │   ├── [RED] adapters/       // lớp truy cập DB async/sync
│       │   ├── [RED] management/     // lệnh quản lý tùy chỉnh
│       │   ├── [RED] migrations/     // migration cụ thể app khoj
│       │   ├── [RED] models/         // model Django (user, agent, logs…)
│       │   └── [WHITE] seeds/insurance_defaults.json // seed data cho sản phẩm bảo hiểm
│       ├── [RED] integrations/       // tích hợp bên thứ ba
│       │   └── [RED] chatwoot.py     // integration Chatwoot support
│       ├── [RED] utils/              // tiện ích chung
│       │   ├── [RED] cli.py          // parser CLI
│       │   ├── [RED] config.py       // config schema
│       │   ├── [RED] constants.py    // hằng số toàn hệ thống
│       │   ├── [RED] helpers.py      // helper functions
│       │   ├── [RED] initialization.py // chuẩn bị môi trường runtime
│       │   ├── [RED] state.py        // state chia sẻ toàn ứng dụng
│       │   └── [WHITE] insurance_validators.py // validate dữ liệu hợp đồng, claim form
│       ├── [RED] search_filter/      // filter truy vấn tìm kiếm
│       │   ├── [RED] date_filter.py  // filter theo thời gian
│       │   ├── [RED] file_filter.py  // filter theo loại file
│       │   ├── [RED] word_filter.py  // filter theo từ khoá
│       │   └── [WHITE] policy_filter.py // filter theo số hợp đồng/loại sản phẩm
│       ├── [RED] search_type/
│       │   ├── [RED] text_search.py  // search thuần text
│       │   └── [WHITE] policy_search.py // search chuyên sản phẩm/điều khoản bảo hiểm
│       └── [WHITE] domain_insurance/ // mô-đun domain bảo hiểm
│           ├── [WHITE] personas.py           // định nghĩa persona tư vấn viên
│           ├── [WHITE] response_templates.py // template trả lời chuẩn hoá
│           ├── [WHITE] workflows.py          // mô tả nghiệp vụ (báo giá, gia hạn, bồi thường)
│           └── [WHITE] compliance.py         // luật tuân thủ, kiểm duyệt nội dung
├── [RED] tests/                     // bộ kiểm thử
│   ├── [RED] conftest.py            // fixture chung
│   ├── [RED] helpers.py             // tiện ích kiểm thử
│   ├── [RED] test_agents.py         // test agent pipeline
│   ├── [RED] test_api_automation.py // test automation API
│   ├── [RED] test_cli.py            // test CLI
│   ├── [RED] test_client.py         // test client interface
│   ├── [RED] test_conversation_utils.py // test xử lý hội thoại
│   ├── [RED] test_date_filter.py    // test filter ngày
│   ├── [RED] test_db_lock.py        // test khoá DB
│   ├── [RED] test_docx_to_entries.py// test chuyển DOCX
│   ├── [RED] test_file_filter.py    // test filter file
│   ├── [RED] test_grep_files.py     // test tìm kiếm file
│   ├── [RED] test_helpers.py        // test helper utilities
│   ├── [RED] test_image_to_entries.py // test OCR ảnh
│   ├── [RED] test_markdown_to_entries.py // test chuyển Markdown
│   ├── [RED] test_multiple_users.py // test multi-user
│   ├── [RED] test_online_chat_actors.py // test actor chat trực tuyến
│   ├── [RED] test_online_chat_director.py // test director orchestration
│   ├── [RED] test_org_to_entries.py // test Org-mode
│   ├── [RED] test_orgnode.py        // test org node parser
│   ├── [RED] test_pdf_to_entries.py // test chuyển PDF
│   ├── [RED] test_plaintext_to_entries.py // test text thuần
│   ├── [RED] test_text_search.py    // test tìm kiếm text
│   ├── [RED] test_word_filter.py    // test filter từ khoá
│   └── [WHITE] test_insurance_workflows.py // test kịch bản bảo hiểm end-to-end
└── [WHITE] deployments/             // tài liệu triển khai theo domain bảo hiểm
    ├── [WHITE] terraform_insurance.md   // ghi chú IaC hạ tầng bảo hiểm
    └── [WHITE] k8s_insurance_overlay/   // overlay cấu hình Kubernetes riêng cho insurance
