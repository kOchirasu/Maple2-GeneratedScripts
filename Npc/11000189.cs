using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000189: Sylvia
/// </summary>
public class _11000189 : NpcScript {
    internal _11000189(INpcScriptContext context) : base(context) {
        Id = 30;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0831180407000830$ 
                // - Can I help you? 
                return true;
            case 30:
                // $script:0831180407000833$ 
                // - I was sickly and weak as a child. Moving to $map:02000076$ improved my health tremendously. 
                switch (selection) {
                    // $script:0831180407000834$
                    // - Where did you live before?
                    case 0:
                        Id = 31;
                        return false;
                }
                return true;
            case 31:
                // $script:0831180407000835$ 
                // - Oh, near $map:02000100$. Have you been there? It's always kinda... overcast. Not sure why. 
                // $script:0831180407000836$ 
                // - $MyPCName$, if you haven't bought a house, you should consider one in $map:02000076$. 
                return true;
            default:
                return true;
        }
    }
}
