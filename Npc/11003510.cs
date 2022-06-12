using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11003510: Gradio
/// </summary>
public class _11003510 : NpcScript {
    protected override int First() {
        // TODO: RandomPick 30;40;50;60
    }

    // Select 0:
    // $script:0816160115009016$
    // - Let's get to business.
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (30, 0):
                // $script:0816160115009017$
                // - It's great having friends to hang out with.
                return -1;
            case (40, 0):
                // $script:0816160115009018$
                // - I used to work with a friend who loved monsters. I helped my friend's dream come true...
                return -1;
            case (50, 0):
                // $script:0816160115009019$
                // - There are no bad monsters.
                return -1;
            case (60, 0):
                // $script:0816160115009020$
                // - Why not take a stroll with a little friend?
                return -1;
        }
        
        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (30, 0) => NpcTalkButton.Close,
            (40, 0) => NpcTalkButton.Close,
            (50, 0) => NpcTalkButton.Close,
            (60, 0) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
