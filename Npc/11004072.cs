using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004072: Suspicious Tree
/// </summary>
public class _11004072 : NpcScript {
    internal _11004072(INpcScriptContext context) : base(context) {
        Id = 10;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0619202207010170$ 
                // - ...
                return true;
            case 10:
                // $script:0619202207010171$ 
                // - ...
                // $script:0619202207010172$ 
                // - ...
                switch (selection) {
                    // $script:0619202207010173$
                    // - ...
                    case 0:
                        Id = 31;
                        return false;
                }
                return true;
            case 31:
                // $script:0619202207010174$ 
                // - ...
                switch (selection) {
                    // $script:0619202207010175$
                    // - ...
                    case 0:
                        Id = 32;
                        return false;
                }
                return true;
            case 32:
                // $script:0619202207010176$ 
                // - ...
                switch (selection) {
                    // $script:0619202207010177$
                    // - Huh. I didn't know trees could scream.
                    case 0:
                        Id = 33;
                        return false;
                }
                return true;
            case 33:
                // $script:0619202207010178$ 
                // - Well obviously I'm not a tree! How did you even spot me? I'm here on a secret mission!
                switch (selection) {
                    // $script:0619202207010179$
                    // - You one of Frey's men?
                    case 0:
                        Id = 40;
                        return false;
                    // $script:0619202207010180$
                    // - Did the empress send you?
                    case 1:
                        Id = 50;
                        return false;
                    // $script:0619202207010181$
                    // - Liar.
                    case 2:
                        Id = 60;
                        return false;
                }
                return true;
            case 40:
                // $script:0619202207010182$ 
                // - I'm trying to keep a low profile here. Can't you pretend you didn't see me and just move along?
                return true;
            case 50:
                // $script:0619202207010183$ 
                // - You aren't worthy to even speak of her!
                return true;
            case 60:
                // $script:0619202207010184$ 
                // - Stop blathering. I'm on duty. Get out of here now, before you regret it.
                return true;
            default:
                return true;
        }
    }
}
