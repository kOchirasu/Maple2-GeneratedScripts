using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000171: Kono
/// </summary>
public class _11000171 : NpcScript {
    protected override int First() {
        // TODO: RandomPick 20;30;50
    }

    // Select 0:
    // $script:0831180407000714$
    // - What brings you here?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (20, 0):
                // $script:0831180407000717$
                // - I told you, I sent all the remaining iron ore on a Goldus Express truck to $map:02000001$. Go there! 
                return -1;
            case (30, 0):
                // $script:0831180407000718$
                // - There's junk, and then there's trash. Some people are so shameless that they think they can get money for their trash. I can't stand deluded fools like that.
                return -1;
            case (50, 0):
                // $script:0323164907008122$
                // - If you've got scrap metal, we can do business. Otherwise, I got too much on my mind to waste talking to you. Those scoundrels are ruining the neighborhood...
                switch (selection) {
                    // $script:0323164907008123$
                    // - How's business?
                    case 0:
                        return 51;
                }
                return -1;
            case (51, 0):
                // $script:0323164907008124$
                // - Well, let's see. Ralph's goons moved in, took over the yard, and ran off my best workers. What do you think?
                return 51;
            case (51, 1):
                // $script:0323164907008125$
                // - My business is in sorry shape thanks to them.
                return -1;
        }

        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (20, 0) => NpcTalkButton.Close,
            (30, 0) => NpcTalkButton.Close,
            (50, 0) => NpcTalkButton.SelectableDistractor,
            (51, 0) => NpcTalkButton.Next,
            (51, 1) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
