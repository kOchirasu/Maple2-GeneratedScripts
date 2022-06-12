using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11003501: Rosa
/// </summary>
public class _11003501 : NpcScript {
    protected override int First() {
        // TODO: RandomPick 30;50
    }

    // Select 0:
    // $script:0816160115008978$
    // - How may I help you?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (30, 0):
                // $script:0816160115008979$
                // - If I'm going to get into Team Mushroom, I've got to study hard!
                return -1;
            case (50, 0):
                // $script:0816160115008981$
                // - I want to be best friends with all kinds of monsters. That's what Team Mushroom is all about, right?
                return -1;
        }
        
        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (30, 0) => NpcTalkButton.Close,
            (50, 0) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
