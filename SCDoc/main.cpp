#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include <stdarg.h>
#include <fstream>

#include "SCDoc.h"
#include <nlohmann/json.hpp>

using json = nlohmann::json;

void error(const char* fmt, ...) {
    fprintf(stderr, "ERROR: ");
    va_list vargs;
    va_start(vargs, fmt);
    vfprintf(stderr, fmt, vargs);
    fflush(stderr);
    va_end(vargs);
}

void post(const char* fmt, ...) {
    va_list vargs;
    va_start(vargs, fmt);
    vfprintf(stderr, fmt, vargs);
    fflush(stderr);
    va_end(vargs);
}

// Convert DocNode tree to JSON recursively
json doc_node_to_json(DocNode* n) {
    if (!n) {
        return nullptr;
    }
    
    json j;
    j["id"] = n->id;
    
    if (n->text) {
        j["text"] = n->text;
    }
    
    if (n->n_childs > 0) {
        j["children"] = json::array();
        for (int i = 0; i < n->n_childs; i++) {
            j["children"].push_back(doc_node_to_json(n->children[i]));
        }
    }
    
    return j;
}

// Write JSON to file
bool write_json_to_file(const json& j, const char* filename) {
    std::ofstream outfile(filename);
    if (!outfile.is_open()) {
        error("Could not open output file: %s\n", filename);
        return false;
    }
    
    outfile << j.dump(2); // Pretty print with 2-space indent
    outfile.close();
    
    if (outfile.fail()) {
        error("Error writing to file: %s\n", filename);
        return false;
    }
    
    return true;
}

int main(int argc, char** argv) {
    if (argc > 1) {
        DocNode* n = nullptr;
        const char* json_output_file = nullptr;
        const char* input_file = nullptr;
        int parse_mode = SCDOC_PARSE_FULL;
        
        // Parse command line arguments
        int i = 1;
        while (i < argc) {
            if (strcmp(argv[i], "--partial") == 0) {
                parse_mode = SCDOC_PARSE_PARTIAL;
                i++;
            } else if (strcmp(argv[i], "--metadata") == 0) {
                parse_mode = SCDOC_PARSE_METADATA;
                i++;
            } else if (strcmp(argv[i], "--json") == 0) {
                if (i + 1 < argc) {
                    json_output_file = argv[i + 1];
                    i += 2;
                } else {
                    fprintf(stderr, "Error: --json requires an output filename\n");
                    return 1;
                }
            } else {
                input_file = argv[i];
                i++;
            }
        }
        
        if (!input_file) {
            fprintf(stderr, "Usage: %s [--partial|--metadata] [--json output.json] inputfile.schelp\n", argv[0]);
            fprintf(stderr, "Options:\n");
            fprintf(stderr, "  --partial     Parse body only (partial mode)\n");
            fprintf(stderr, "  --metadata    Parse metadata only\n");
            fprintf(stderr, "  --json FILE   Write parse tree to FILE as JSON\n");
            return 1;
        }
        
        n = scdoc_parse_file(input_file, parse_mode);
        if (n) {
            // Always dump to stdout
            doc_node_dump(n);
            
            // Additionally write JSON if requested
            if (json_output_file) {
                json j = doc_node_to_json(n);
                if (write_json_to_file(j, json_output_file)) {
                    fprintf(stderr, "\nJSON output written to: %s\n", json_output_file);
                } else {
                    doc_node_free_tree(n);
                    return 1;
                }
            }
            
            doc_node_free_tree(n);
        } else {
            return 1;
        }
    } else {
        fprintf(stderr, "Usage: %s [--partial|--metadata] [--json output.json] inputfile.schelp\n", argv[0]);
        fprintf(stderr, "Options:\n");
        fprintf(stderr, "  --partial     Parse body only (partial mode)\n");
        fprintf(stderr, "  --metadata    Parse metadata only\n");
        fprintf(stderr, "  --json FILE   Write parse tree to FILE as JSON\n");
    }
    return 0;
}
