using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001708: Tinchai
/// </summary>
public class _11001708 : NpcScript {
    internal _11001708(INpcScriptContext context) : base(context) {
        Id = 30;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0728022507006960$ 
                // - Mm? Yes? 
                return true;
            case 30:
                // $script:0805021607007079$ 
                // - I feel... sluggish... 
                switch (selection) {
                    // $script:0805021607007080$
                    // - Why's that?
                    case 0:
                        Id = 31;
                        return false;
                }
                return true;
            case 31:
                // $script:0805021607007081$ 
                // - Do you know how long it's been since I had a good nap? Ever since we got here, I've been so busy that I haven't had time to train, let alone get my beauty sleep. 
                switch (selection) {
                    // $script:0805021607007082$
                    // - Go take a nap now.
                    case 0:
                        Id = 32;
                        return false;
                }
                return true;
            case 32:
                // $script:0805021607007083$ 
                // - It wouldn't do any good. I have to get myself good and tired from training, or I can't doze off. So it'll just have to wait!
<font color="#909090">(She gives a cheerful laugh.)</font> 
                return true;
            default:
                return true;
        }
    }
}
