using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000001: Manovich
/// </summary>
public class _11000001 : NpcScript {
    protected override int First() {
        // TODO: RandomPick 10;20
    }

    // Select 0:
    // $script:0831180407000001$
    // - $MyPCName$, what is it?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (10, 0):
                // $script:0831180407000003$
                // - ...And this knucklehead, where in the world is he?
                switch (selection) {
                    // $script:0831180407000004$
                    // - What is it?
                    case 0:
                        return 11;
                }
                return -1;
            case (11, 0):
                // $script:0831180407000005$
                // - My son is a bit... no, he's very hard-headed. I lost my patience with him, and well... He stormed out of the house and hasn't returned yet.
                return 11;
            case (11, 1):
                // $script:0831180407000006$
                // - Sigh... People are right when they say parenting is the world's hardest job.
                return -1;
            case (20, 0):
                // $script:0831180407000007$
                // - It's a beautiful day today. Hopefully it'll stay that way... 
                return 20;
            case (20, 1):
                // $script:0831180407000008$
                // - As the elder of this village, I'm doing my best to keep its residents safe. But there's little I could do about the seal of the Land of Darkness breaking, and now something terrible seems to happen every day.
                return 20;
            case (20, 2):
                // $script:0831180407000009$
                // - The only wish I have now is for peace. $MyPCName$, I'm relying on you for that.
                return -1;
        }

        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (10, 0) => NpcTalkButton.SelectableDistractor,
            (11, 0) => NpcTalkButton.Next,
            (11, 1) => NpcTalkButton.Close,
            (20, 0) => NpcTalkButton.Next,
            (20, 1) => NpcTalkButton.Next,
            (20, 2) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
