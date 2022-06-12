using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004066: Mysterious Luditionist
/// </summary>
public class _11004066 : NpcScript {
    protected override int First() {
        return 10;
    }

    // Select 0:
    // $script:0619202207010127$
    // - ...
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (10, 0):
                // $script:0619202207010128$
                // - ...
                return 10;
            case (10, 1):
                // $script:0619202207010129$
                // - Tch! Don't tell me I got caught... Your senses are sharp, I'll give you that.
                switch (selection) {
                    // $script:0619202207010130$
                    // - Why are you hiding here?
                    case 0:
                        return 31;
                }
                return -1;
            case (31, 0):
                // $script:0619202207010131$
                // - This place, the $map:02000262$, was created by us, the luditionists. I'm taking a quick peek to ensure everything is running smoothly. And by smoothly, I mean with lots of exciting incidents.
                return -1;
            case (32, 0):
                // $script:0619202207010132$
                // - A world without incidents is boring, hmm? We don't want a boring world.
                switch (selection) {
                    // $script:0619202207010133$
                    // - What does a luditionist do?
                    case 0:
                        return 33;
                }
                return -1;
            case (33, 0):
                // $script:0619202207010134$
                // - Hush, now. Don't ask too many questions or you'll get hurt. Let's just say that we're trying to make things more fun.
                return -1;
        }
        
        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (10, 0) => NpcTalkButton.Next,
            (10, 1) => NpcTalkButton.SelectableDistractor,
            (31, 0) => NpcTalkButton.Close,
            (32, 0) => NpcTalkButton.SelectableDistractor,
            (33, 0) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
