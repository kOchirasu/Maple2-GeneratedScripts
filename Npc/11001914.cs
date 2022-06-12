using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001914: Lennon
/// </summary>
public class _11001914 : NpcScript {
    protected override int First() {
        return 20;
    }

    // Select 0:
    // $script:1116181807007413$
    // - Welcome. 
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (20, 0):
                // $script:1116181807007415$
                // - Katvan and I will meet again. 
                return -1;
        }

        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (20, 0) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
