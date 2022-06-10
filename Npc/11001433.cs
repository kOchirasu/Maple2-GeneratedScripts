using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001433: Azore
/// </summary>
public class _11001433 : NpcScript {
    internal _11001433(INpcScriptContext context) : base(context) {
        Id = 40;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:1216230507005187$ 
                // - Is this your first time in the desert? It's beautiful...
                return true;
            case 40:
                // $script:1216230507005191$ 
                // - When we first came to the desert from the city, I was stunned by the beauty. 
                switch (selection) {
                    // $script:1216230507005192$
                    // - You don't miss the city?
                    case 0:
                        Id = 41;
                        return false;
                }
                return true;
            case 41:
                // $script:1216230507005193$ 
                // - I miss my old friends, but there's something about the desert sands under a full moon. It's terrifyingly dangerous... but undeniably beautiful.
                switch (selection) {
                    // $script:1216230507005194$
                    // - Dangerous? How?
                    case 0:
                        Id = 42;
                        return false;
                }
                return true;
            case 42:
                // $script:1216230507005195$ 
                // - The sandstorms. If you aren't careful, they'll come and sweep away your loved ones. 
                // $script:1216230507005196$ 
                // - The others say I was just dreaming, but I know it was real. One day, I'll meet them.
                return true;
            default:
                return true;
        }
    }
}
