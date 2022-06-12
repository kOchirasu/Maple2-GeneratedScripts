using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11003155: Rumi
/// </summary>
public class _11003155 : NpcScript {
    protected override int First() {
        return 30;
    }

    // Select 0:
    // $script:0306155707008043$
    // - Can I help you?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (30, 0):
                // $script:0306155707008046$
                // - My sisters say I'm prettier than any flower. I agree.
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
