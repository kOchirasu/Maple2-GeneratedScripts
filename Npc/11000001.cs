using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000001: Manovich
/// </summary>
public class _11000001 : NpcScript {
    internal _11000001(INpcScriptContext context) : base(context) {
        // TODO: RandomPick 10;20
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0831180407000001$ 
                // - $MyPCName$, what is it?
                return true;
            case 10:
                // $script:0831180407000003$ 
                // - ...And this knucklehead, where in the world is he?
                switch (selection) {
                    // $script:0831180407000004$
                    // - What is it?
                    case 0:
                        Id = 11;
                        return false;
                }
                return true;
            case 11:
                // $script:0831180407000005$ 
                // - My son is a bit... no, he's very hard-headed. I lost my patience with him, and well... He stormed out of the house and hasn't returned yet.
                // $script:0831180407000006$ 
                // - Sigh... People are right when they say parenting is the world's hardest job.
                return true;
            case 20:
                // $script:0831180407000007$ 
                // - It's a beautiful day today. Hopefully it'll stay that way... 
                // $script:0831180407000008$ 
                // - As the elder of this village, I'm doing my best to keep its residents safe. But there's little I could do about the seal of the Land of Darkness breaking, and now something terrible seems to happen every day.
                // $script:0831180407000009$ 
                // - The only wish I have now is for peace. $MyPCName$, I'm relying on you for that.
                return true;
            default:
                return true;
        }
    }
}
