.PHONY: help sync run clean

help: ## 🚀 Visa tillgängliga kommandon
	@echo "🔧 Minidemo Rapport - Kommandon:"
	@echo ""
	@echo "📦 Dependency management:"
	@echo "  make sync     Installera/uppdatera dependencies med uv"
	@echo ""
	@echo "🎯 Applikation:"
	@echo "  make run      Starta Streamlit-appen"
	@echo ""
	@echo "🧹 Underhåll:"
	@echo "  make clean    Ta bort genererade filer"
	@echo ""
	@echo "💡 Tips: Aktivera venv först: source uv/bin/activate"

sync: ## 📦 Installera dependencies med uv
	@echo "📦 Installerar dependencies..."
	uv pip install -r requirements.txt
	@echo "✅ Dependencies installerade!"

run: ## 🚀 Starta Streamlit-appen
	@echo "🚀 Startar Streamlit-appen..."
	streamlit run app.py

clean: ## 🧹 Ta bort genererade filer
	@echo "🧹 Tar bort genererade filer..."
	rm -f rapport_output.docx
	@echo "✅ Städat!"
