using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001632: Eupheria
/// </summary>
public class _11001632 : NpcScript {
    protected override int First() {
        return 10;
    }

    // Select 0:
    // $script:0517100407006134$
    // - Sniff... 
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (10, 0):
                // $script:0517100407006135$
                // - This is all my doing... 
                return -1;
        }

        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (10, 0) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
