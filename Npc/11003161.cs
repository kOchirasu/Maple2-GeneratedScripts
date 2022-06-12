using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11003161: Troy
/// </summary>
public class _11003161 : NpcScript {
    protected override int First() {
        return 20;
    }

    // Select 0:
    // $script:0306155707008067$
    // - Can I help you?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (20, 0):
                // $script:0306155707008069$
                // - If you love flowers so much, then go pick them yourself. These aren't for you.
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
