using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001070: Flan
/// </summary>
public class _11001070 : NpcScript {
    protected override int First() {
        return 30;
    }

    // Select 0:
    // $script:0831180407003647$
    // - Nice to meet you.
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (30, 0):
                // $script:0831180407003650$
                // - Do you know how rewarding it is to see the seeds you've sown grow into beautiful flowers?
                return -1;
        }

        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (30, 0) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
