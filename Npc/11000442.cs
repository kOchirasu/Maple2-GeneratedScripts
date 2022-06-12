using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000442: Cathy Mart Employee
/// </summary>
public class _11000442 : NpcScript {
    protected override int First() {
        // TODO: RandomPick 20;30
    }

    // Select 0:
    // $script:0831180407001859$
    // - Can I help you?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (20, 0):
                // $script:0831180407001861$
                // - I don't want to talk. I got ripped off by my boss, and then I almost got killed by robbers. My life sucks!
                return -1;
            case (30, 0):
                // $script:0831180407001862$
                // - Do you want to know what the owner of Cathy Mart is like? The worst, that's what! 
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
