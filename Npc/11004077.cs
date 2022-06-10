using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004077: Blackstar Hideout
/// </summary>
public class _11004077 : NpcScript {
    internal _11004077(INpcScriptContext context) : base(context) {
        Id = 10;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0619202207010220$ 
                // - <font color="#909090">(Pressing your ear to the door, you hear some Blackstar gangsters talking.)</font>
                return true;
            case 10:
                // $script:0619202207010221$ 
                // - <font color="#909090">(Pressing your ear to the door, you hear some Blackstar gangsters talking.)</font>
                // $script:0619202207010222$ 
                // - <font color="#f45342">The big party's tomorrow. You get that cake for Haren yet?</font>
                // $script:0619202207010223$ 
                // - <font color="#41f441">I'm workin' on it! That bakery ya sent me to ain't exactly quick. You know they take orders years in advance?</font>
                // $script:0619202207010224$ 
                // - <font color="#41f441">Wait a sec. This is for Haren? I told 'em to put Min's name on the cake!</font>
                // $script:0619202207010225$ 
                // - <font color="#f45342">You <b>what?!</b> Chen's gonna smash my head in when he sees we messed up Haren's birthday bash!</font>
                return true;
            default:
                return true;
        }
    }
}
