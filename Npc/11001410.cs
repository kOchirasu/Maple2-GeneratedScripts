using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001410: Dona
/// </summary>
public class _11001410 : NpcScript {
    internal _11001410(INpcScriptContext context) : base(context) {
        Id = 40;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:1217205907005407$ 
                // - You came to gawk at the Meerkat Patrols? 
                return true;
            case 40:
                // $script:1222203907005494$ 
                // - We all trust and rely on each other in the Meerkat Patrol. You could say we're a big happy family.
                switch (selection) {
                    // $script:1222203907005495$
                    // - What's the secret to your camaraderie?
                    case 0:
                        Id = 41;
                        return false;
                }
                return true;
            case 41:
                // $script:1222203907005496$ 
                // - It's all thanks to our hardworking captain. We all look up to good old Captain $npcName:11001408[gender:0]$! 
                // $script:1222203907005497$ 
                // - Since you're here, you should say hi to him. I bet he'll have some good advice for you.
                return true;
            default:
                return true;
        }
    }
}
