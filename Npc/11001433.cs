using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001433: Azore
/// </summary>
public class _11001433 : NpcScript {
    protected override int First() {
        return 40;
    }

    // Select 0:
    // $script:1216230507005187$
    // - Is this your first time in the desert? It's beautiful...
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (40, 0):
                // $script:1216230507005191$
                // - When we first came to the desert from the city, I was stunned by the beauty. 
                switch (selection) {
                    // $script:1216230507005192$
                    // - You don't miss the city?
                    case 0:
                        return 41;
                }
                return -1;
            case (41, 0):
                // $script:1216230507005193$
                // - I miss my old friends, but there's something about the desert sands under a full moon. It's terrifyingly dangerous... but undeniably beautiful.
                switch (selection) {
                    // $script:1216230507005194$
                    // - Dangerous? How?
                    case 0:
                        return 42;
                }
                return -1;
            case (42, 0):
                // $script:1216230507005195$
                // - The sandstorms. If you aren't careful, they'll come and sweep away your loved ones. 
                return 42;
            case (42, 1):
                // $script:1216230507005196$
                // - The others say I was just dreaming, but I know it was real. One day, I'll meet them.
                return -1;
        }
        
        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (40, 0) => NpcTalkButton.SelectableDistractor,
            (41, 0) => NpcTalkButton.SelectableDistractor,
            (42, 0) => NpcTalkButton.Next,
            (42, 1) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
