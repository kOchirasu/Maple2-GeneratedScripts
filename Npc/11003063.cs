using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11003063: Surmany
/// </summary>
public class _11003063 : NpcScript {
    internal _11003063(INpcScriptContext context) : base(context) {
        // TODO: RandomPick 30;40
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0102155907007646$ 
                // - What do you want?
                return true;
            case 30:
                // $script:0102155907007647$ 
                // - You must conserve your energy in the cold. That's why I don't talk much. Just so you know. 
                return true;
            case 40:
                // $script:0207083707007919$ 
                // - Oh look, it's $MyPCName$ the worrywart. What do you want?
                switch (selection) {
                    // $script:0207083707007920$
                    // - I need burning breaths!
                    case 0:
                        Id = 41;
                        return false;
                    // $script:0207083707007921$
                    // - Why are you so much smaller than the other snowfolks?
                    case 1:
                        Id = 42;
                        return false;
                }
                return true;
            case 41:
                // $script:0207083707007922$ functionID=1 
                // - There you go. This is because you got those materials for me, you know. Helping others pays off!
                return true;
            case 42:
                // $script:0207083707007923$ 
                // - Excuse me? Hey, that's none of your business! And I'm not small... the others are just really big!
                //   <font color="#909090">(He's gotten sulky. I don't think he'll want to talk to me anymore.)</font>
                return true;
            default:
                return true;
        }
    }
}
