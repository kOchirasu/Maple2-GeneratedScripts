using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004066: Mysterious Luditionist
/// </summary>
public class _11004066 : NpcScript {
    internal _11004066(INpcScriptContext context) : base(context) {
        Id = 10;
        // TODO: RandomPick 10
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0619202207010127$ 
                // - ...
                return true;
            case 10:
                // $script:0619202207010128$ 
                // - ...
                // $script:0619202207010129$ 
                // - Tch! Don't tell me I got caught... Your senses are sharp, I'll give you that.
                switch (selection) {
                    // $script:0619202207010130$
                    // - Why are you hiding here?
                    case 0:
                        Id = 31;
                        return false;
                }
                return true;
            case 31:
                // $script:0619202207010131$ 
                // - This place, the $map:02000262$, was created by us, the luditionists. I'm taking a quick peek to ensure everything is running smoothly. And by smoothly, I mean with lots of exciting incidents.
                return true;
            case 32:
                // $script:0619202207010132$ 
                // - A world without incidents is boring, hmm? We don't want a boring world.
                switch (selection) {
                    // $script:0619202207010133$
                    // - What does a luditionist do?
                    case 0:
                        Id = 33;
                        return false;
                }
                return true;
            case 33:
                // $script:0619202207010134$ 
                // - Hush, now. Don't ask too many questions or you'll get hurt. Let's just say that we're trying to make things more fun.
                return true;
            default:
                return true;
        }
    }
}
