using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001281: Ishura
/// </summary>
public class _11001281 : NpcScript {
    protected override int First() {
        return 30;
    }

    // Select 0:
    // $script:1211023307004972$
    // - Hm... Wait.
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (30, 0):
                // $script:1209020507004851$
                // - I don't understand him... I really don't...
                return -1;
        }
        
        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (30, 0) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
