using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004520: Mayo
/// </summary>
public class _11004520 : NpcScript {
    protected override int First() {
        return 10;
    }

    // Select 0:
    // $script:0102174210002222$
    // - Non-stop service to $map:02020041$ in Kritias will be departing soon.
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (10, 0):
                // $script:0102174210002223$
                // - Non-stop service to $map:02020041$ in Kritias will be departing soon.
                return 10;
            case (10, 1):
                // $script:0102174210002224$
                // - Kritias is no place for pushovers. You know that, right? Well, if you're sure, hop aboard and I'll get you to $map:02020041$.
                switch (selection) {
                    // $script:0102174210002225$
                    // - Take me to $map:02020041$!
                    case 0:
                        return 11;
                }
                return -1;
            case (11, 0):
                // functionID=1 
                // $script:0102174210002226$
                // - All right. Away we go!
                return -1;
        }

        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (10, 0) => NpcTalkButton.Next,
            (10, 1) => NpcTalkButton.SelectableDistractor,
            (11, 0) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
