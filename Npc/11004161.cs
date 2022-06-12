using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004161: Nurse Nora
/// </summary>
public class _11004161 : NpcScript {
    protected override int First() {
        return 10;
    }

    // Select 0:
    // $script:0730132107010547$
    // - Are you here to see the doctor? Do you have an appointment?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (10, 0):
                // $script:0730132107010548$
                // - Sigh, no time to rest. Too many patients to get to.
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
