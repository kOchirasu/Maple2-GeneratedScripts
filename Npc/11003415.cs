using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11003415: Hero's Tomb
/// </summary>
public class _11003415 : NpcScript {
    protected override int First() {
        return 10;
    }

    // Select 0:
    // $script:0623153207008576$
    // - <i>Here lies Red Fox, courageous warrior of $map:02000051$. He laid down his life while defending our people from the forces of darkness, and for that he will always be remembered.</i>
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (10, 0):
                // $script:0623180607008578$
                // - <i>Here lies Red Fox, courageous warrior of $map:02000051$. He laid down his life while defending our people from the forces of darkness, and for that he will always be remembered.</i>
                return -1;
        }

        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (10, 0) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
