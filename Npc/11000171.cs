using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000171: Kono
/// </summary>
public class _11000171 : NpcScript {
    internal _11000171(INpcScriptContext context) : base(context) {
        // TODO: RandomPick 20;30;50
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0831180407000714$ 
                // - What brings you here? 
                return true;
            case 20:
                // $script:0831180407000717$ 
                // - I told you, I sent all the remaining iron ore on a Goldus Express truck to $map:02000001$. Go there!  
                return true;
            case 30:
                // $script:0831180407000718$ 
                // - There's junk, and then there's trash. Some people are so shameless that they think they can get money for their trash. I can't stand deluded fools like that. 
                return true;
            case 50:
                // $script:0323164907008122$ 
                // - If you've got scrap metal, we can do business. Otherwise, I got too much on my mind to waste talking to you. Those scoundrels are ruining the neighborhood... 
                switch (selection) {
                    // $script:0323164907008123$
                    // - How's business?
                    case 0:
                        Id = 51;
                        return false;
                }
                return true;
            case 51:
                // $script:0323164907008124$ 
                // - Well, let's see. Ralph's goons moved in, took over the yard, and ran off my best workers. What do you think? 
                // $script:0323164907008125$ 
                // - My business is in sorry shape thanks to them. 
                return true;
            default:
                return true;
        }
    }
}
