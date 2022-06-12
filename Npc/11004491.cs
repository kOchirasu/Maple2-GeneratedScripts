using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004491: Kharadi
/// </summary>
public class _11004491 : NpcScript {
    protected override int First() {
        return 10;
    }

    // Select 0:
    // $script:1227192907012327$
    // - Shh! Quiet! They'll hear us!
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (10, 0):
                // $script:1227192907012328$
                // - Shh! Quiet! They'll hear us!
                return 10;
            case (10, 1):
                // $script:1227192907012329$
                // - I stumbled upon this place quite by accident. I never imagined there might be a large robot factory here.
                return 10;
            case (10, 2):
                // $script:1227192907012330$
                // - See there? The robots are made without any intervention from human factory workers. And with such speed, no less! This explains the endless forces that the Tairen army has managed to field.
                switch (selection) {
                    // $script:1227192907012331$
                    // - Should I blow this place up, then?
                    case 0:
                        return 11;
                }
                return -1;
            case (11, 0):
                // $script:1227192907012332$
                // - I'm afraid this is but one small corner of the whole facility. What's more, if any part of the factory is destroyed, it's repaired automatically within minutes.
                return 11;
            case (11, 1):
                // $script:1227192907012333$
                // - Any attempt to destroy this place would fail to put any sizable dent in their production capabilities. It would, however, mark our presence on Kritias as a clear threat. A threat that they would feel compelled to wipe out.
                return 11;
            case (11, 2):
                // $script:1227192907012334$
                // - Instead of striking out blindly, we need to understand the full scope of this facility... and what it will take to destroy it once and for all.
                switch (selection) {
                    // $script:0114164107012723$
                    // - Okay.
                    case 0:
                        return 12;
                }
                return -1;
            case (12, 0):
                // $script:0114164107012724$
                // - I need to learn more about this facility.
                return -1;
        }
        
        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (10, 0) => NpcTalkButton.Next,
            (10, 1) => NpcTalkButton.Next,
            (10, 2) => NpcTalkButton.SelectableDistractor,
            (11, 0) => NpcTalkButton.Next,
            (11, 1) => NpcTalkButton.Next,
            (11, 2) => NpcTalkButton.SelectableDistractor,
            (12, 0) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
