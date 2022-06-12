using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004077: Blackstar Hideout
/// </summary>
public class _11004077 : NpcScript {
    protected override int First() {
        return 10;
    }

    // Select 0:
    // $script:0619202207010220$
    // - <font color="#909090">(Pressing your ear to the door, you hear some Blackstar gangsters talking.)</font>
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (10, 0):
                // $script:0619202207010221$
                // - <font color="#909090">(Pressing your ear to the door, you hear some Blackstar gangsters talking.)</font>
                return 10;
            case (10, 1):
                // $script:0619202207010222$
                // - <font color="#f45342">The big party's tomorrow. You get that cake for Haren yet?</font>
                return 10;
            case (10, 2):
                // $script:0619202207010223$
                // - <font color="#41f441">I'm workin' on it! That bakery ya sent me to ain't exactly quick. You know they take orders years in advance?</font>
                return 10;
            case (10, 3):
                // $script:0619202207010224$
                // - <font color="#41f441">Wait a sec. This is for Haren? I told 'em to put Min's name on the cake!</font>
                return 10;
            case (10, 4):
                // $script:0619202207010225$
                // - <font color="#f45342">You <b>what?!</b> Chen's gonna smash my head in when he sees we messed up Haren's birthday bash!</font>
                return -1;
        }
        
        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (10, 0) => NpcTalkButton.Next,
            (10, 1) => NpcTalkButton.Next,
            (10, 2) => NpcTalkButton.Next,
            (10, 3) => NpcTalkButton.Next,
            (10, 4) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
