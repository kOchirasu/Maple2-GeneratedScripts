using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001191: Joanna
/// </summary>
public class _11001191 : NpcScript {
    internal _11001191(INpcScriptContext context) : base(context) {
        Id = 30;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:1016202007004164$ 
                // - I wish I could cast my worries into the wind...  
                return true;
            case 30:
                // $script:1016202007004167$ 
                // - I wish it would all just be over...   
                switch (selection) {
                    // $script:1016202007004168$
                    // - What's wrong?
                    case 0:
                        Id = 31;
                        return false;
                }
                return true;
            case 31:
                // $script:1016202007004170$ 
                // - It's been one disaster after another, and I'm just too tired to fight anymore. Money is ruining my life. If I could live without it, I would've quit already. 
                // $script:1016202007004171$ 
                // - I got transferred to another department because of an argument with the head of the broadcasting station over my program. Journalism used to be about integrity! It was about telling the truth, not just covering what makes money! I just can't do it anymore.  
                // $script:1022192907004266$ 
                // - I soldier on and cover what they tell me, acting like there's nothing wrong. But every day I die a little inside. Someone's got to stand up to them, I know that! But if I do, they'll just replace me with another yes-man... 
                return true;
            default:
                return true;
        }
    }
}
