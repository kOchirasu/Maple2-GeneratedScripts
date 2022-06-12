using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11003503: Ranshu
/// </summary>
public class _11003503 : NpcScript {
    protected override int First() {
        // TODO: RandomPick 30;40;50
    }

    // Select 0:
    // $script:0816160115008986$
    // - What is it?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (30, 0):
                // $script:0816160115008987$
                // - The Team Mushroom has people all over the world. You'll find them wherever you find monsters!
                return -1;
            case (40, 0):
                // $script:0816160115008988$
                // - Team Mushroom and Dryad Co. don't have much in common. Dryad sells the tools of the pet-taming trade. Team Mushroom is working to protect the world from devastation, and unite all peoples across the nation!
                return -1;
            case (50, 0):
                // $script:0816160115008989$
                // - I work alone, but I'll be in need of a partner in the future.
                switch (selection) {
                    // $script:0816211715009063$
                    // - What about me?
                    case 0:
                        // TODO: goto 51,52
                        return -1;
                }
                return -1;
            case (51, 0):
                // $script:0816211715009064$
                // - Hey... Are you serious...?
                return -1;
            case (52, 0):
                // $script:0816211715009065$
                // - Not right now. But... maybe later.
                return -1;
        }

        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (30, 0) => NpcTalkButton.Close,
            (40, 0) => NpcTalkButton.Close,
            (50, 0) => NpcTalkButton.SelectableDistractor,
            (51, 0) => NpcTalkButton.Close,
            (52, 0) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
