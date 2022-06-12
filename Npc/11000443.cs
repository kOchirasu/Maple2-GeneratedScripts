using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000443: Cathy Mart Employee
/// </summary>
public class _11000443 : NpcScript {
    protected override int First() {
        // TODO: RandomPick 20;30
    }

    // Select 0:
    // $script:0831180407001863$
    // - Can I help you?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (20, 0):
                // $script:0831180407001865$
                // - If we don't get that money back, it's coming out of <i>my</i> paycheck...
                return -1;
            case (30, 0):
                // $script:0831180407001866$
                // - I don't know who's worse, the boss or the robbers.
                return -1;
        }
        
        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (20, 0) => NpcTalkButton.Close,
            (30, 0) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
