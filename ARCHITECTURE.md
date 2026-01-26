# KENSAI Sphinx Container - Architecture

## Container Architecture

```
┌─────────────────────────────────────────────────────────────────┐
│                    KENSAI Sphinx Container                      │
│                    (kensai-sphinx:latest)                       │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  ┌───────────────────────────────────────────────────────┐    │
│  │            Python 3.13 Alpine Linux                    │    │
│  │                 (Base Image)                           │    │
│  └───────────────────────────────────────────────────────┘    │
│                         │                                       │
│                         ▼                                       │
│  ┌───────────────────────────────────────────────────────┐    │
│  │          System Dependencies Layer                     │    │
│  │  • Graphviz (diagram generation)                       │    │
│  │  • Build tools (gcc, musl-dev)                        │    │
│  │  • Git (version control)                              │    │
│  │  • Fonts (TrueType fonts)                             │    │
│  └───────────────────────────────────────────────────────┘    │
│                         │                                       │
│                         ▼                                       │
│  ┌───────────────────────────────────────────────────────┐    │
│  │        Python Packages Layer (80+ packages)            │    │
│  ├───────────────────────────────────────────────────────┤    │
│  │  Core Tools:                                           │    │
│  │  ├─ Sphinx 7.0+ (documentation generator)             │    │
│  │  ├─ pdoc3 (API docs)                                  │    │
│  │  └─ pyan3 (call graphs)                               │    │
│  │                                                        │    │
│  │  Extensions (60+):                                     │    │
│  │  ├─ sphinx-autoapi (auto API docs)                    │    │
│  │  ├─ sphinx-autobuild (live reload)                    │    │
│  │  ├─ sphinx-copybutton (copy code)                     │    │
│  │  ├─ myst-parser (Markdown support)                    │    │
│  │  ├─ nbsphinx (Jupyter notebooks)                      │    │
│  │  └─ 55+ more extensions...                            │    │
│  │                                                        │    │
│  │  Themes:                                               │    │
│  │  ├─ sphinx-rtd-theme (Read the Docs)                  │    │
│  │  ├─ furo (Modern design)                              │    │
│  │  ├─ sphinx-book-theme (Book style)                    │    │
│  │  └─ pydata, material, and more...                     │    │
│  │                                                        │    │
│  │  Tools & Utilities:                                    │    │
│  │  ├─ graphviz (Python bindings)                        │    │
│  │  ├─ markdown (Markdown support)                       │    │
│  │  └─ pydot, gprof2dot, etc.                            │    │
│  └───────────────────────────────────────────────────────┘    │
│                         │                                       │
│                         ▼                                       │
│  ┌───────────────────────────────────────────────────────┐    │
│  │          Documentation Layer                           │    │
│  │  /sphinx/docs/                                         │    │
│  │  ├─ conf.py (Sphinx configuration)                    │    │
│  │  ├─ index.rst (Main page)                             │    │
│  │  ├─ sphinx-packages.rst (Package list)                │    │
│  │  ├─ quick-reference.rst (Quick guide)                 │    │
│  │  ├─ tutorials/ (Tutorial section)                     │    │
│  │  │  ├─ sphinx-basics.rst                              │    │
│  │  │  ├─ themes.rst                                     │    │
│  │  │  ├─ extensions.rst                                 │    │
│  │  │  └─ packages/ (Package tutorials)                  │    │
│  │  ├─ examples/ (Example section)                       │    │
│  │  │  ├─ basic-example.rst                              │    │
│  │  │  ├─ api-docs-example.rst                           │    │
│  │  │  ├─ jupyter-example.rst                            │    │
│  │  │  └─ graphviz-example.rst                           │    │
│  │  └─ _build/html/ (Generated HTML)                     │    │
│  └───────────────────────────────────────────────────────┘    │
│                         │                                       │
│                         ▼                                       │
│  ┌───────────────────────────────────────────────────────┐    │
│  │          Web Server Layer                              │    │
│  │  Python http.server                                    │    │
│  │  • Serves /sphinx/docs/_build/html/                   │    │
│  │  • Listens on 0.0.0.0:8080                            │    │
│  │  • Auto-starts on container launch                    │    │
│  └───────────────────────────────────────────────────────┘    │
│                         │                                       │
└─────────────────────────┼───────────────────────────────────────┘
                          │
                          ▼
                   Port 8080 (Exposed)
                          │
                          ▼
              ┌───────────────────────┐
              │   Host Machine        │
              │   http://localhost:8080│
              └───────────────────────┘
```

## Data Flow

### Documentation Build Process

```
Developer
    │
    ▼
┌─────────────────────┐
│  Build Container    │
│  (build.bat/.sh)    │
└──────────┬──────────┘
           │
           ▼
┌─────────────────────┐
│  Docker Build       │
│  Process            │
└──────────┬──────────┘
           │
           ├─► Install System Dependencies
           │
           ├─► Install Python Packages
           │
           ├─► Copy Documentation Source
           │
           ├─► Run sphinx-build
           │       │
           │       ├─► Parse RST/MD files
           │       ├─► Generate HTML
           │       ├─► Create search index
           │       └─► Copy static files
           │
           └─► Create Container Image
                    │
                    ▼
            ┌──────────────────┐
            │  kensai-sphinx   │
            │  Docker Image    │
            └──────────────────┘
```

### Runtime Process

```
User
  │
  ├─► docker run kensai-sphinx
  │
  ▼
┌─────────────────────┐
│  Container Starts   │
└──────────┬──────────┘
           │
           ▼
┌─────────────────────┐
│  start-server.sh    │
└──────────┬──────────┘
           │
           ▼
┌─────────────────────┐
│  Python HTTP Server │
│  (port 8080)        │
└──────────┬──────────┘
           │
           ▼
┌─────────────────────┐
│  Serve HTML Files   │
│  from _build/html/  │
└──────────┬──────────┘
           │
           ▼
      User's Browser
   http://localhost:8080
```

## Usage Patterns

### Pattern 1: View Container Documentation

```
┌──────────┐         ┌────────────────┐         ┌─────────┐
│  User    │────────►│  Container     │────────►│ Browser │
└──────────┘         │  (Docs Server) │         └─────────┘
                     └────────────────┘
                            │
                            ▼
                     Built-in Documentation
```

### Pattern 2: Generate Project Documentation

```
┌──────────┐         ┌────────────────┐         ┌─────────────┐
│ Project  │────────►│  Container     │────────►│ Project     │
│ (Volume) │  mount  │  (Sphinx Tool) │  output │ _build/html │
└──────────┘         └────────────────┘         └─────────────┘
                            │
                            ▼
                     sphinx-build command
```

### Pattern 3: Development with Auto-Rebuild

```
┌──────────┐         ┌────────────────┐         ┌─────────┐
│ Source   │────────►│  Container     │────────►│ Browser │
│ (Watch)  │  change │  (Auto-build)  │  reload │ (Live)  │
└──────────┘         └────────────────┘         └─────────┘
     ▲                      │                         │
     │                      ▼                         │
     │              sphinx-autobuild                  │
     │                      │                         │
     └──────────────────────┴─────────────────────────┘
                      Live Preview
```

## File System Layout

```
Container Filesystem:
/
├── sphinx/                     # Main working directory
│   ├── docs/                   # Documentation source
│   │   ├── conf.py            # Sphinx configuration
│   │   ├── *.rst              # Documentation files
│   │   ├── _static/           # Static assets
│   │   ├── _templates/        # Templates
│   │   └── _build/            # Generated output
│   │       └── html/          # HTML documentation
│   │           ├── index.html
│   │           ├── *.html
│   │           ├── _static/
│   │           └── search/
│   └── start-server.sh        # Startup script
│
├── usr/
│   ├── local/
│   │   ├── bin/
│   │   │   ├── sphinx-build   # Sphinx commands
│   │   │   ├── sphinx-autobuild
│   │   │   └── pdoc3
│   │   └── lib/
│   │       └── python3.13/
│   │           └── site-packages/  # Python packages
│   └── bin/
│       └── graphviz           # System tools
│
└── etc/
    └── apk/                   # Package info
```

## Network Architecture

```
┌─────────────────────────────────────────┐
│         Host Machine                    │
│                                         │
│  ┌───────────────────────────────────┐ │
│  │     Docker Engine                 │ │
│  │                                   │ │
│  │  ┌─────────────────────────────┐ │ │
│  │  │  kensai-sphinx Container    │ │ │
│  │  │                             │ │ │
│  │  │  ┌───────────────────────┐  │ │ │
│  │  │  │  Python HTTP Server   │  │ │ │
│  │  │  │  0.0.0.0:8080         │  │ │ │
│  │  │  └───────────┬───────────┘  │ │ │
│  │  │              │              │ │ │
│  │  └──────────────┼──────────────┘ │ │
│  │                 │                │ │
│  └─────────────────┼────────────────┘ │
│                    │                  │
│          Port Mapping (8080:8080)    │
│                    │                  │
└────────────────────┼──────────────────┘
                     │
                     ▼
              localhost:8080
                     │
                     ▼
              User's Browser
```

## Volume Mounting Patterns

### Read-Only Documentation

```
Host                          Container
┌──────────────┐             ┌──────────────┐
│ /docs        │────────────►│ /project/docs│
│ (read-only)  │   mount     │              │
└──────────────┘             └──────────────┘
```

### Read-Write (Build Output)

```
Host                          Container
┌──────────────┐             ┌──────────────┐
│ /docs        │◄───────────►│ /project/docs│
│ (read-write) │   mount     │              │
└──────────────┘             └──────────────┘
     │                              │
     └─► _build/ created here ◄─────┘
```

## Extension Architecture

```
┌─────────────────────────────────────────┐
│           Sphinx Core                   │
├─────────────────────────────────────────┤
│                                         │
│  ┌────────────────────────────────┐    │
│  │     Built-in Extensions        │    │
│  │  • autodoc                     │    │
│  │  • napoleon                    │    │
│  │  • viewcode                    │    │
│  │  • intersphinx                 │    │
│  │  • graphviz                    │    │
│  └────────────────────────────────┘    │
│                                         │
│  ┌────────────────────────────────┐    │
│  │   Third-party Extensions       │    │
│  │  • sphinx-autoapi              │    │
│  │  • sphinx-copybutton           │    │
│  │  • myst-parser                 │    │
│  │  • nbsphinx                    │    │
│  │  • 50+ more...                 │    │
│  └────────────────────────────────┘    │
│                                         │
│  ┌────────────────────────────────┐    │
│  │          Themes                │    │
│  │  • RTD Theme                   │    │
│  │  • Furo                        │    │
│  │  • Book Theme                  │    │
│  │  • PyData Theme                │    │
│  │  • Material Theme              │    │
│  └────────────────────────────────┘    │
│                                         │
└─────────────────────────────────────────┘
```

## Component Interactions

```
┌─────────────┐
│  Developer  │
└──────┬──────┘
       │
       ├─────────────────────────────┐
       │                             │
       ▼                             ▼
┌─────────────┐              ┌──────────────┐
│ Write Docs  │              │ Run Commands │
│ (.rst/.md)  │              │ (docker run) │
└──────┬──────┘              └──────┬───────┘
       │                             │
       ▼                             │
┌─────────────┐                      │
│   Sphinx    │◄─────────────────────┘
│   Parser    │
└──────┬──────┘
       │
       ├──────────────┬──────────────┬
       ▼              ▼              ▼
┌──────────┐   ┌──────────┐   ┌──────────┐
│Extensions│   │ Themes   │   │Graphviz  │
└─────┬────┘   └────┬─────┘   └────┬─────┘
      │             │              │
      └─────────────┴──────────────┘
                    │
                    ▼
            ┌──────────────┐
            │ HTML Output  │
            └──────┬───────┘
                   │
                   ▼
            ┌──────────────┐
            │ HTTP Server  │
            └──────┬───────┘
                   │
                   ▼
            ┌──────────────┐
            │   Browser    │
            └──────────────┘
```

## Build vs Runtime

### Build Time

```
Dockerfile ──► Docker Build ──► Image Created
    │              │                  │
    ├─ FROM        ├─ Pull base      │
    ├─ RUN         ├─ Execute        ├─ Layers
    ├─ COPY        ├─ Copy files     ├─ Cached
    └─ CMD         └─ Set command    └─ Tagged
```

### Runtime

```
docker run ──► Container Start ──► Server Running
    │              │                     │
    ├─ Image       ├─ Initialize        ├─ Serving
    ├─ Ports       ├─ Mount volumes     ├─ Logging
    ├─ Volumes     ├─ Start server      └─ Ready
    └─ Env vars    └─ Port 8080
```

---

This architecture provides:
- **Modularity**: Separate layers for different concerns
- **Flexibility**: Multiple usage patterns supported
- **Performance**: Layer caching for fast rebuilds
- **Portability**: Self-contained documentation
- **Scalability**: Can run multiple instances
- **Maintainability**: Clear separation of components
